'''Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].'''

l=[5,6,77,45,22,12,24]
n=[i for i in l if i%2!=0 ]
print(n)