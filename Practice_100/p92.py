'''Please write a program which accepts a string from console and print the characters that have even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld'''
n=input()
l=[i for (j,i) in enumerate(n) if j%2==0]
print(''.join(l))