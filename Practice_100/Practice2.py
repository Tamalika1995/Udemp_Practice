'''Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the
following input is supplied to the program: 8 Then, the output should be:40320'''
#using function
from math import  factorial
x=int(input("enter the no: "))
print(factorial(x))
#using for loop
n = int(input("enter another no ")) #input() function takes input as string type
                #int() converts it to integer type
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)