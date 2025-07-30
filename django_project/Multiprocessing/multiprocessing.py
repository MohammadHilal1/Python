import time
import multiprocessing
import concurrent.futures
from PIL import Image, ImageFilter

# Multiprocessing is a technique that allows to create multiple independent processes, each with its own memory space and Python interpreter, to perform tasks in aprallel
# It is used for CPU bound tasks like file/image processing and performing large numeric computations
# Program without multiprocessing This program will take ~10 seconds to finish as the function is executed synchronously 10 times

def do_something(seconds):
    print(f"Going to sleep for {seconds} second(s)")
    time.sleep(seconds)
    print(f"Done sleeping...{seconds}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    for _ in range(10):
        do_something(1)
    
    finish_time = time.perf_counter()

    print("time taken:", round(finish_time-start_time, 2))

# Program with multiprocessing This pragram will take 1-2 seconds as the function is executed asynchronously 10 times
if __name__ == "__main__":
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [5,4,3,2,1]
        results = [executor.submit(do_something, sec) for sec in seconds]

        for f in concurrent.futures.as_completed(results):
            print(f.result())
    
    finish_time = time.perf_counter()

    print("time taken:", round(finish_time-start_time, 2))

# Here is a practical example of using multiprocessing.Here we are going to take each image and process it and store it into a folder.
# If we execute it without multiprocessing it may take 15-20 seconds but if we execute this with multiprocessing it may take ~5 seconds

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]
size = [1200, 1200]
def process_image(image_name):
    try:
        image = Image.open(image_name)
        image = image.filter(ImageFilter.GaussianBlur(15))
        image.thumbnail(size)
        image.save(f'processed/{image_name}')
        print(f'{image_name} was processed')
    except Exception as e:
        print(Exception, "File not found")

if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_image, img_names)

    finish = time.perf_counter()

    print("Time taken :", round(finish-start, 2))
