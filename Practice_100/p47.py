'''Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

'''
from math import pi

class Circle():
    def __init__(self,r):
        self.r=r

    def area(self):
        a=pi*(self.r**2)
        return a
c=Circle(4)
print(c.area())