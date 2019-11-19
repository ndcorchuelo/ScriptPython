# Module supplies classes for manipulating dates and times
import datetime as dt
import calendar as cl

yr, mo, dd = 2012, 12, 21 

X = dt.date(yr, mo, dd)

print (X)

hr, mm, ss, ms = 12, 21, 12, 21

M = dt.time(hr, mm, ss, ms)

print (M)
now = dt.datetime.now() + dt.timedelta(days=50) # adding Dates and Times in Python

print (now)

# Get weekday of first day of the month and number of days in month
Z = cl.monthrange(now.year,now.month) 

# Tuesday   1
# Wednesday 2
# Thursday  3
# Friday    4
# Saturday  5
# Sunday    5
# Monday    7

print(Z)

print(type(Z)) # View type of data

yr, mo, dd = now.year-1,now.month-1 or 12, Z[1]

T = dt.date(yr, mo, dd) # the last day of the month

print(T)
