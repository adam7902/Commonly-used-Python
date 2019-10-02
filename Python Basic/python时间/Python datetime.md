**[Python DateTime](https://www.pythonprogramming.in/date-time.html)**



[TOC]



#### 打印当前日期和时间

[Displays the current date and time using time module](https://www.pythonprogramming.in/date-time/displays-the-current-time-and-date-using-time-module.html)


```python
#Python's program that displays the current time and date in various format.
 
#import time module
import time
from time import gmtime, strftime
 
t = time.localtime()
print (time.asctime(t))
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(strftime("%A", gmtime()))
print(strftime("%D", gmtime()))
print(strftime("%B", gmtime()))
print(strftime("%y", gmtime()))
 
# Convert seconds into GMT date
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(1234567890)))
```

    Sat Sep 21 08:09:50 2019
    Sat, 21 Sep 2019 00:09:50 +0000
    Saturday
    09/21/19
    September
    19
    Fri, 13 Feb 2009 23:31:30 +0000


#### 把天、小时、分钟转换成秒

[Convert Days, Hours, Minutes into Seconds](https://www.pythonprogramming.in/date-time/convert-days-hours-minutes-into-seconds.html)


```python
#Python's program to convert number of days, hours, minutes and seconds to seconds.
##

#Define the constants
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

#Read the inputs from user
days = int(input("Enter number of Days: "))
hours = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))

#Calculate the days, hours, minutes and seconds
total_seconds = days * SECONDS_PER_DAY
total_seconds = total_seconds + (hours * SECONDS_PER_HOUR)
total_seconds = total_seconds + (minutes * SECONDS_PER_MINUTE)
total_seconds = total_seconds + seconds

#Display the result
print("Total number of seconds: ", "%d" % (total_seconds))
```

    Enter number of Days: 5
    Enter number of Hours: 23
    Enter number of Minutes: 12
    Enter number of Seconds: 6
    Total number of seconds:  515526


#### 使用panda在python中获取当前日期和时间

[Using Pandas get current date and time in python](https://www.pythonprogramming.in/date-time/using-pandas-get-current-date-and-time-in-python.html)


```python
# Python's program to get current date time using pandas.

import pandas as pd
print(pd.datetime.now())
print(pd.datetime.now().date())
print(pd.datetime.now().year)
print(pd.datetime.now().month)
print(pd.datetime.now().day)
print(pd.datetime.now().hour)
print(pd.datetime.now().minute)
print(pd.datetime.now().second)
print(pd.datetime.now().microsecond)
```

    2019-09-21 08:13:52.961000
    2019-09-21
    2019
    9
    21
    8
    13
    52
    961000


#### 将字符串转换为datetime对象

[Python program to convert string into datetime object](https://www.pythonprogramming.in/date-time/python-program-to-convert-string-into-datetime-object.html)


```python
# Python's program to convert string into date time
from datetime import datetime
from dateutil import parser

d1 = "Jan 7 2019  1:15PM"
d2 = "2019 Jan 7  1:33PM"

# If you know date format
date1 = datetime.strptime(d1, '%b %d %Y %I:%M%p')
print(type(date1))
print(date1)

# If you don't know date format
date2 = parser.parse(d2)
print(type(date2))
print(date2)
```

    <class 'datetime.datetime'>
    2019-01-07 13:15:00
    <class 'datetime.datetime'>
    2019-01-07 13:33:00


#### 获取当前时间(以毫秒为单位)

[Get current time in milliseconds in Python](https://www.pythonprogramming.in/date-time/get-current-time-in-milliseconds-in-python.html)


```python
# Python's program to get time in milliseconds.
import time
 
milliseconds = int(round(time.time() * 1000))
print(milliseconds)
```

    1569025167444


#### 获取当前的日期时间在MST, EST, UTC, GMT和HST格式

[Get current date time in MST, EST, UTC, GMT and HST](https://www.pythonprogramming.in/date-time/get-current-time-in-mst-est-utc-and-gmt.html)


```python
# Python's program to get current time MST EST UTC GMT HST
from datetime import datetime
from pytz import timezone
 
mst = timezone('MST')
print("Time in MST:", datetime.now(mst))
 
est = timezone('EST')
print("Time in EST:", datetime.now(est))
 
utc = timezone('UTC')
print("Time in UTC:", datetime.now(utc))
 
gmt = timezone('GMT')
print("Time in GMT:", datetime.now(gmt))
 
hst = timezone('HST')
print("Time in HST:", datetime.now(hst))
```

    Time in MST: 2019-09-20 17:20:42.246000-07:00
    Time in EST: 2019-09-20 19:20:42.246000-05:00
    Time in UTC: 2019-09-21 00:20:42.246000+00:00
    Time in GMT: 2019-09-21 00:20:42.247000+00:00
    Time in HST: 2019-09-20 14:20:42.247000-10:00


#### 用Python从给定的日期中获取星期几

[Get the day of week from given a date in Python](https://www.pythonprogramming.in/date-time/get-the-day-of-week-from-given-a-date-in-python.html)


```python
# Python's program to get the day of week of today or given date.
import datetime
 
dayofweek = datetime.date(2010, 6, 16).strftime("%A")
print("星期:", dayofweek)
# weekday Monday is 0 and Sunday is 6
print("weekday():", datetime.date(2010, 6, 16).weekday())
 
# isoweekday() Monday is 1 and Sunday is 7
print("isoweekday()", datetime.date(2010, 6, 16).isoweekday())
 
dayofweek = datetime.datetime.today().strftime("%A")
print(dayofweek)
print("weekday():", datetime.datetime.today().weekday())
print("isoweekday()", datetime.datetime.today().isoweekday())
```

    星期: Wednesday
    weekday(): 2
    isoweekday() 3
    Saturday
    weekday(): 5
    isoweekday() 6


#### 如何计算两个datetime对象之间的时间差?

[How to calculate the time difference between two datetime objects?](https://www.pythonprogramming.in/date-time/how-to-calculate-the-time-difference-between-two-datetime-objects.html)


```python
# Python's program to calculate time difference between two datetime objects.
 
import datetime
from datetime import timedelta
 
datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2016-04-16 10:01:28.585'
date2 = '2016-03-10 09:56:28.067'
diff = datetime.datetime.strptime(date1, datetimeFormat)\
    - datetime.datetime.strptime(date2, datetimeFormat)

print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
```

    Difference: 37 days, 0:05:00.518000
    Days: 37
    Microseconds: 518000
    Seconds: 300


#### 将(Unix)时间戳秒转换为日期和时间字符串

[Convert (Unix) timestamp seconds to date and time string](https://www.pythonprogramming.in/date-time/convert-unix-timestamp-seconds-to-date-and-time-string.html)


```python
# Python's program to convert (Unix) timestamp to date and time string.
from datetime import datetime
 
dateStr = datetime.fromtimestamp(1415419007).strftime("%A, %B %d, %Y %I:%M:%S")
print(type(dateStr))
print(dateStr)
```

    <class 'str'>
    Saturday, November 08, 2014 11:56:47


#### 将数据时间对象转换为Unix(时间戳)

[Convert data time object to Unix (time-stamp)](https://www.pythonprogramming.in/date-time/convert-data-time-object-to-unix-time-stamp.html)


```python
# Python's program to convert datatime object to Unix Timestamp
 
import datetime
import time
 
# Saturday, October 10, 2015 10:10:00 AM
date_obj = datetime.datetime(2015, 10, 10, 10, 10)
print("Unix Timestamp: ", (time.mktime(date_obj.timetuple())))
```

    Unix Timestamp:  1444443000.0


#### 在当前日期时间上添加年、月、日、时、分、秒

[Add N number of Year, Month, Day, Hour, Minute, Second to current date-time](https://www.pythonprogramming.in/date-time/add-n-number-of-year-month-day-hour-minute-second-to-current-date-time.html)


```python
# Python's program to add N year month day hour min sec to date.
 
import datetime
from dateutil.relativedelta import relativedelta
 
add_days = datetime.datetime.today() + relativedelta(days=+6)
add_months = datetime.datetime.today() + relativedelta(months=+6)
add_years = datetime.datetime.today() + relativedelta(years=+6)
 
add_hours = datetime.datetime.today() + relativedelta(hours=+6)
add_mins = datetime.datetime.today() + relativedelta(minutes=+6)
add_seconds = datetime.datetime.today() + relativedelta(seconds=+6)
 
print("Current Date Time:", datetime.datetime.today())
print("Add 6 days:", add_days)
print("Add 6 months:", add_months)
print("Add 6 years:", add_years)
print("Add 6 hours:", add_hours)
print("Add 6 mins:", add_mins)
print("Add 6 seconds:", add_seconds)
```

    Current Date Time: 2019-09-21 08:26:17.029000
    Add 6 days: 2019-09-27 08:26:17.029000
    Add 6 months: 2020-03-21 08:26:17.029000
    Add 6 years: 2025-09-21 08:26:17.029000
    Add 6 hours: 2019-09-21 14:26:17.029000
    Add 6 mins: 2019-09-21 08:32:17.029000
    Add 6 seconds: 2019-09-21 08:26:23.029000


#### 获取指定开始日期和结束日期之间的日期范围

[Get range of dates between specified start and end date](https://www.pythonprogramming.in/date-time/get-range-of-dates-between-specified-start-and-end-date.html)


```python
# Python's program to display all dates between two dates.
import datetime

start = datetime.datetime.strptime("2019-09-15", "%Y-%m-%d")
end = datetime.datetime.strptime("2019-09-30", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))

for date_object in date_array:
    print(date_object.strftime("%Y-%m-%d"))
```

    2019-09-15
    2019-09-16
    2019-09-17
    2019-09-18
    2019-09-19
    2019-09-20
    2019-09-21
    2019-09-22
    2019-09-23
    2019-09-24
    2019-09-25
    2019-09-26
    2019-09-27
    2019-09-28
    2019-09-29


#### 用当前日期时间减去年、月、日、时、分、秒

[Subtract N number of Year, Month, Day, Hour, Minute, Second to current date-time](https://www.pythonprogramming.in/date-time/subtract-n-number-of-year-month-day-hour-minute-second-to-current-date-time.html)


```python
# Python's program to subtract N year month day hour min sec to date.
import datetime
from dateutil.relativedelta import relativedelta
 
sub_days = datetime.datetime.today() + relativedelta(days=-6)
sub_months = datetime.datetime.today() + relativedelta(months=-6)
sub_years = datetime.datetime.today() + relativedelta(years=-6)
 
sub_hours = datetime.datetime.today() + relativedelta(hours=-6)
sub_mins = datetime.datetime.today() + relativedelta(minutes=-6)
sub_seconds = datetime.datetime.today() + relativedelta(seconds=-6)
 
print("Current Date Time:", datetime.datetime.today())
print("Subtract 6 days:", add_days)
print("Subtract 6 months:", add_months)
print("Subtract 6 years:", add_years)
print("Subtract 6 hours:", add_hours)
print("Subtract 6 mins:", add_mins)
print("Subtract 6 seconds:", add_seconds)
```

    Current Date Time: 2019-09-21 08:28:36.708000
    Subtract 6 days: 2019-09-27 08:26:17.029000
    Subtract 6 months: 2020-03-21 08:26:17.029000
    Subtract 6 years: 2025-09-21 08:26:17.029000
    Subtract 6 hours: 2019-09-21 14:26:17.029000
    Subtract 6 mins: 2019-09-21 08:32:17.029000
    Subtract 6 seconds: 2019-09-21 08:26:23.029000


从指定的年份和月份中获取每月第一天的工作日和每月的天数

[Get weekday of first day of the month and number of days in month, from specified year and month](https://www.pythonprogramming.in/date-time/weekday-of-first-day-of-the-month-and-number-of-days-in-month-for-the-specified-year-and-month.html)


```python
# Python's program to weekday of first day of the month and
# number of days in month, for the specified year and month.
import calendar
 
print("Year:2002 - Month:2")
month_range = calendar.monthrange(2002, 2)
print("Weekday of first day of the month:", month_range[0])
print("Number of days in month:", month_range[1])
print()
print("Year:2010 - Month:5")
month_range = calendar.monthrange(2010, 5)
print("Weekday of first day of the month:", month_range[0])
print("Number of days in month:", month_range[1])
```

    Year:2002 - Month:2
    Weekday of first day of the month: 4
    Number of days in month: 28
    
    Year:2010 - Month:5
    Weekday of first day of the month: 5
    Number of days in month: 31


#### 打印特定年份的所有星期一

[Print all Monday's of a specific year](https://www.pythonprogramming.in/date-time/print-all-monday-of-a-specific-year.html)


```python
# Python's program to print all Monday's of a specific year
from datetime import date, timedelta
 
year = 2018
date_object = date(year, 1, 1)
date_object += timedelta(days=1-date_object.isoweekday())
 
while date_object.year == year:
    print(date_object)
    date_object += timedelta(days=7)
```

    2018-01-01
    2018-01-08
    2018-01-15
    2018-01-22
    2018-01-29
    2018-02-05
    2018-02-12
    2018-02-19
    2018-02-26
    2018-03-05
    2018-03-12
    2018-03-19
    2018-03-26
    2018-04-02
    2018-04-09
    2018-04-16
    2018-04-23
    2018-04-30
    2018-05-07
    2018-05-14
    2018-05-21
    2018-05-28
    2018-06-04
    2018-06-11
    2018-06-18
    2018-06-25
    2018-07-02
    2018-07-09
    2018-07-16
    2018-07-23
    2018-07-30
    2018-08-06
    2018-08-13
    2018-08-20
    2018-08-27
    2018-09-03
    2018-09-10
    2018-09-17
    2018-09-24
    2018-10-01
    2018-10-08
    2018-10-15
    2018-10-22
    2018-10-29
    2018-11-05
    2018-11-12
    2018-11-19
    2018-11-26
    2018-12-03
    2018-12-10
    2018-12-17
    2018-12-24
    2018-12-31


#### 打印特定年份的日历

[Print calendar of specific year](https://www.pythonprogramming.in/date-time/print-calendar-of-current-year.html)


```python
# Python's program to print calendar of specific year.
 
import calendar
cal_display = calendar.TextCalendar(calendar.MONDAY)
# Year: 2019
# Column width: 1
# Lines per week: 1 
# Number of spaces between month columns: 0
# No. of months per column: 2
print(cal_display.formatyear(2019, 1, 1, 0, 2))
```

                       2019
    
          January               February
    Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6               1  2  3
     7  8  9 10 11 12 13   4  5  6  7  8  9 10
    14 15 16 17 18 19 20  11 12 13 14 15 16 17
    21 22 23 24 25 26 27  18 19 20 21 22 23 24
    28 29 30 31           25 26 27 28
    
           March                 April
    Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
                 1  2  3   1  2  3  4  5  6  7
     4  5  6  7  8  9 10   8  9 10 11 12 13 14
    11 12 13 14 15 16 17  15 16 17 18 19 20 21
    18 19 20 21 22 23 24  22 23 24 25 26 27 28
    25 26 27 28 29 30 31  29 30
    
            May                   June
    Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
           1  2  3  4  5                  1  2
     6  7  8  9 10 11 12   3  4  5  6  7  8  9
    13 14 15 16 17 18 19  10 11 12 13 14 15 16
    20 21 22 23 24 25 26  17 18 19 20 21 22 23
    27 28 29 30 31        24 25 26 27 28 29 30
    
            July                 August
    Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7            1  2  3  4
     8  9 10 11 12 13 14   5  6  7  8  9 10 11
    15 16 17 18 19 20 21  12 13 14 15 16 17 18
    22 23 24 25 26 27 28  19 20 21 22 23 24 25
    29 30 31              26 27 28 29 30 31
    
         September              October
    Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
                       1      1  2  3  4  5  6
     2  3  4  5  6  7  8   7  8  9 10 11 12 13
     9 10 11 12 13 14 15  14 15 16 17 18 19 20
    16 17 18 19 20 21 22  21 22 23 24 25 26 27
    23 24 25 26 27 28 29  28 29 30 31
    30
    
          November              December
    Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
                 1  2  3                     1
     4  5  6  7  8  9 10   2  3  4  5  6  7  8
    11 12 13 14 15 16 17   9 10 11 12 13 14 15
    18 19 20 21 22 23 24  16 17 18 19 20 21 22
    25 26 27 28 29 30     23 24 25 26 27 28 29
                          30 31


​    

#### 如何从月号中得到月名?

[How I can get the month name from the month number?](https://www.pythonprogramming.in/date-time/how-can-i-get-the-month-name-from-the-month-number.html)


```python
# Python's program to get the month name from the month number
import calendar
import datetime
 
# Month name from number
print("Month name from number 5:")
month_num = 1
month_abre = datetime.date(2015, month_num, 1).strftime('%b')
month_name = datetime.date(2015, month_num, 1).strftime('%B')
print("Short Name:", month_abre)
print("Full  Name:", month_name)
 
print("\nList of all months from calendar")
# Print list of all months from calendar
for month_val in range(1, 13):
    print(calendar.month_abbr[month_val], "-", calendar.month_name[month_val])
```

    Month name from number 5:
    Short Name: Jan
    Full  Name: January
    
    List of all months from calendar
    Jan - January
    Feb - February
    Mar - March
    Apr - April
    May - May
    Jun - June
    Jul - July
    Aug - August
    Sep - September
    Oct - October
    Nov - November
    Dec - December


#### 如何开始和结束一个星期的日期从一个给定的日期?

[How to get start and end of date of a week from a given date?](https://www.pythonprogramming.in/date-time/how-to-get-start-and-end-of-week-data-from-a-given-date.html)


```python
# Python's program to get start and end of week
from datetime import datetime, timedelta
 
date_str = '2018-01-14'
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
 
start_of_week = date_obj - timedelta(days=date_obj.weekday())  # Monday
end_of_week = start_of_week + timedelta(days=6)  # Sunday
print(start_of_week)
print(end_of_week)
```

    2018-01-08 00:00:00
    2018-01-14 00:00:00


#### 根据当前日期查找前一个和下一个星期一的日期

[Find the previous and coming Monday's date, based on current date](https://www.pythonprogramming.in/date-time/find-the-previous-and-coming-monday-s-date-based-on-current-date.html)


```python
# Python's program to get last and coming Monday
import datetime
 
today = datetime.date.today()
last_monday = today - datetime.timedelta(days=today.weekday())
coming_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
print("Today:", today)
print("Last Monday:", last_monday)
print("Coming Monday:", coming_monday)
```

    Today: 2019-09-21
    Last Monday: 2019-09-16
    Coming Monday: 2019-09-23


#### 获取当前季度的第一个日期和最后一个日期

[Get First Date and Last Date of Current Quarter](https://www.pythonprogramming.in/date-time/get-first-date-and-last-date-of-current-quarter.html)


```python
# Python's program to get first and last day of Current Quarter Year
from datetime import datetime, timedelta

current_date = datetime.now()
current_quarter = round((current_date.month - 1) // 3 + 1)  # 使用整除//,3个月一个季度
first_date = datetime(current_date.year, 3 * current_quarter - 2, 1)
last_date = datetime(current_date.year, 3 * current_quarter + 1, 1) + timedelta(days=-1)

print("First Day of Quarter:", first_date)
print("Last Day of Quarter:", last_date)
```

    First Day of Quarter: 2019-07-01 00:00:00
    Last Day of Quarter: 2019-09-30 00:00:00



