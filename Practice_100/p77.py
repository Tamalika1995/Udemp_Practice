'''Please write a program to print the running time of execution of "1+1" for 100 times.'''

import datetime

before = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
    print(x)
after = datetime.datetime.now()
execution_time = after - before
print(execution_time.microseconds)