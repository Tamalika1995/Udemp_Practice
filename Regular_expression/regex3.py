import re

r1=re.compile('Bat(wo)?man')##? refer to optional-- the group can be present 0 or 1 times
print(r1.search('Batwoman').group())
print(r1.search('Batman').group())
r2=re.compile('(\d\d\d-)*(\d\d\d-\d\d\d\d)')##? refer to optional--the group can be present o or more times
print(r2.search('090-098-0987').group())
print(r2.search('098-098-098-0987').group())

r1=re.compile('Bat(wo)+man')##+ refer to mandetory--the group can be present 1 or more times
print(r1.search('Batwoman').group())
print(r1.search('Batman'))

##to match special character like + ,*, ? which have a separate meaning in regex we need to add \ before them
r1=re.compile('Bat(\+\*)+man')##+ refer to mandetory--the group can be present multiple times
print(r1.search('Bat+*man').group())

