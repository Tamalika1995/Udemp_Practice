'''Write a method which can calculate square value of number

Hints:
Using the ** operator which can be written as n**p where means n^p
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function'''
def cal_sqrt():
    n = int(input("enter your no --> "))
    return n**n
m=cal_sqrt()
print(m)
print(abs.__doc__)
print(int.__doc__)
print(cal_sqrt.__doc__)