'''Define a class with a generator which can iterate the numbers, which are divisible by 7,
 between a given range 0 and n.
Suppose the following input is supplied to the program:
7
Then, the output should be
0
7
14'''

class A():
    def div_by_seven(self,n):
        for i in range(n+1):
            if i%7==0:
               yield i
obj=A()
gen=obj.div_by_seven(int(input("enter your no : ")))
for i in gen:
    print(i)