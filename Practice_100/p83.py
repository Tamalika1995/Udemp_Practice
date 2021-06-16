'''By using list comprehension, please write a program to print the list after
removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].'''

orig_list = [12,24,35,70,88,120,155]
new_list = [i for (j, i) in enumerate(orig_list) if j not in range(2,5)]
print(new_list)