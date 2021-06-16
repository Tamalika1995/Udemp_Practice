'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
 You are given scores. Store them in a list and find the score of the runner-up.
If the following string is given as input to the program:
5
2 3 6 6 5
Then, the output of the program should be:5'''
n=int(input())
l=[]
for i in range(5):
    m=input("enter score: ")
    l.append(m)
s=sorted(list(set(l)))
print(s[-2])