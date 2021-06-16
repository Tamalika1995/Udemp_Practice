'''Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
L=[]
L=[str(i) for i in range(1000,3001)  for j in str(i) if int(j)%2==0]
'''for i in range(1000,3001):
    for j in str(i):
        if int(j)%2==0:
            L.append(str(i))'''
print(','.join(L))