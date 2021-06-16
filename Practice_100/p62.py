'''The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13'''
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
L=[]
n=int(input())
for i in range(0,n+1):
    L.append(str(fib(i)))
print(','.join(L))
