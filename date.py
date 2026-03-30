import datetime
from time import strftime
today=datetime.date.today()
print(today)
day=today.day
month=today.month
year=today.year
print("<h1>Current Time</h1>")
time=datetime.datetime.now()
time=strftime("%H:%M:%S   %m-%d-%Y")
print(time)
print(day)
print(month)
print(year)