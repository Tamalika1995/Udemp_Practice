'''Write a program which can map() and filter() to make a list whose elements are square
of even number in [1,2,3,4,5,6,7,8,9,10].'''

n=list(map(lambda i:i**2,list(filter(lambda n:n%2==0,[1,2,3,4,5,6,7,8,9,10]))))
print(n)