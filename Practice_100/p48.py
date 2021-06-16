'''Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.'''
from math import pi

class Circle():
    def __init__(self,l,h):
        self.l=l
        self.h=h
    def area(self):
        a=(self.l*self.h)
        return a
c=Circle(4,8)
print(c.area())