'''By using list comprehension, please write a program to print the
list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].'''

l=[12,24,35,70,88,120,155]
n=[i for i in l if i%35!=0]
print(n)

