'''You are given a date. Your task is to find what the day is on that date.
Input

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
08 05 2015
Output
Output the correct day in capital letters.
WEDNESDAY
Hints
Use weekday function of calender module'''
import calendar
l=[i for i in input().split(' ')]
m=int(l[0])
d=int(l[1])
y=int(l[2])
day1=calendar.weekday(y,m,d)
day_name=calendar.day_name[day1]
print(day_name.upper())

