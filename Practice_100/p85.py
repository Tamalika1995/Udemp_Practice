'''By using list comprehension, please write a program to print the list after removing
the 0th,4th,5th numbers in [12,24,35,70,88,120,155]'''
l=[12,24,35,70,88,120,155]

n=[i for (j,i) in enumerate(l) if j!=0 and j!=4 and j!=5]
print(n)