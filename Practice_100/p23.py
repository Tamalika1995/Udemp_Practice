'''Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later

'''
class Car():
    name=input("enter class param")
    def __init__(self,name=None):
        self.name=name
honda=Car(input("enter car name"))
print(f'{honda.name} {Car.name}')
honda1=Car()
print(f'{honda1.name} {Car.name}')