from datetime import datetime, date, time, timedelta

# Display todays date and time 
date = datetime.now()

print(f'Today date is {date.strftime("%d/%M/%Y")} and time is {date.strftime("%H:%M:%S")}')

# Days left to year end
date = datetime.now().date()
year_end = datetime.now().replace(day=31, month=12).date()

print(abs(date - year_end).days)

# Find given date is valid or not
date_str = "2025-07-25"
def is_valid(date_str):
  try:
    datetime.strptime(date_str, "%Y-%m-%d")
    return  True
  except:
    return False

if is_valid(date_str):
  print(f'{date_str} is valid')
else:
  print(f'{date_str} is not valid')

#Age Calculator
date_of_birth = None
while True:
  dt_input = input("Enter your date in YYYY-MM-DD format")
  if is_valid(dt_input):
    date_of_birth = datetime.strptime(dt_input, "%Y-%m-%d")
    print(date_of_birth)
    break
  else:
    print("Invalid date format")
today = datetime.today()
age = today.year - date_of_birth.year

if(today.month, today.day) < (date_of_birth.month, date_of_birth.day):
  age -= 1

print(age)

# Print day of the week on the given date

dt_input = input("Enter your date in YYYY-MM-DD format")
print(datetime.strptime(dt_input, "%Y-%m-%d").strftime("%A"))

# List all mondays in a given month
from datetime import date, timedelta, datetime
year_month = "2025-07"

year = datetime.strptime(year_month, "%Y-%m").year
month = datetime.strptime(year_month, "%Y-%m").month
date_obj = datetime.strptime(year_month, "%Y-%m")
cur_date = date(date_obj.year, date_obj.month, 1)

while(cur_date.weekday() != 0):
  cur_date += timedelta(days=1)

Mondays = []
while cur_date.month == month:
  Mondays.append(cur_date)
  cur_date += timedelta(days=7)
  
for idx, dt in enumerate(Mondays):
  print(f"{idx + 1} Monday on {dt}")

#Time difference Calculator

t1, t2 = "14:00:00", "18:45:00"

t1 = datetime.strptime(t1, "%H:%M:%S")
t2 = datetime.strptime(t2, "%H:%M:%S")

print(t2-t1)

# Is the store open

open_time = "09:00"
close_time = "17:00"

open_time = datetime.strptime(open_time, "%H:%M").time()
close_time = datetime.strptime(close_time, "%H:%M").time()
current_time = datetime.now().time()

if (current_time > open_time) and (current_time < close_time):
  print("Store is open")
else:
  print("Store is closed")

# Print dates between 2 given dates
d1 = "2025-07-31"
d2 = "2025-08-15"

d1 = datetime.strptime(d1, "%Y-%m-%d").date()
d2 = datetime.strptime(d2, "%Y-%m-%d").date()

while (d1 < d2):
  d1 = d1 + timedelta(days=1)
  print(d1)

#Find weekends between two dates
d1 = "2025-07-31"
d2 = "2025-08-22"

d1 = datetime.strptime(d1, "%Y-%m-%d").date()
d2 = datetime.strptime(d2, "%Y-%m-%d").date()

weekends = []
while (d1 < d2):
  if d1.weekday() in [5,6]:
    weekends.append((d1, d1.strftime("%A")))
  d1 = d1 + timedelta(days=1)
if len(weekends) > 0:
  for weekend in weekends:
    print(f"{weekend[1]} on {weekend[0]}")
else:
  print("No weekends")