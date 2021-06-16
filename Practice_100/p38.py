'''With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half
 values in one line and the last half values in one line.'''

t=tuple([1,2,3,4,5,6,7,8,9,10])
l=int(len(t)/2)
print(t[0:l])
print(t[l:len(t)])