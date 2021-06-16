'''Define a function which can generate and print a list where the values are square of numbers
 between 1 and 20 (both included).'''
def print_list():
    L=[i**2 for i in range(1,21)]
    print(L)
print_list()