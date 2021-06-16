'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''
n=input()
s=""
r=0
for i in range(int(4)):
        s+=n
        r+=int(s)
print(r)

