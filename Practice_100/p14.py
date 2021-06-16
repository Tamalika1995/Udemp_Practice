'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

n=input()
u=0
l=0
for i in n:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
print(f'UPPER CASE {u}\nLOWER CASE {l}')