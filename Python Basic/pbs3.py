# display the current date and time.
import datetime as dt
date_time = dt.datetime.now()
print (f"Current date and time : {date_time.strftime('%d-%m-%Y %H:%M:%S')}")
print (date_time.strftime("%d-%m-%Y %H:%M:%S"))

import time
lt = time.localtime()
days = lt.tm_mday
years = lt.tm_year
month = lt.tm_mon
hours = lt.tm_hour
min = lt.tm_min
sec = lt.tm_sec
print(days,month,years, sep="/")
print (hours,min,sec,sep=":")
print(days)