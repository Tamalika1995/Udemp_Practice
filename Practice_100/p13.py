'''Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

n=input()
l=0
d=0
for i in n:
    if i.isalpha():
        l+=1
    elif i.isdigit():
        d+=1
print(f'LETTERS {l}')
print(f'DIGITS {d}')