'''Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
'''
class A():
    def getString(self):
        self.a=input("enter a string:")
    def printString(self):
        while True:
            if self.a.isalpha():
                print(str(self.a).upper())
                break
            else:
                print("Please enter a String contains only character (a-z A-Z)")
                self.getString()
obj=A()
obj.getString()
obj.printString()