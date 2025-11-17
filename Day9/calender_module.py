import calendar
month,day,year=map(int,input().split())
d=calendar.weekday(year, month, day)
day_name = calendar.day_name[d]
print(day_name.upper())


#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
