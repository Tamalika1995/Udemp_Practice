# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name,age):
    # Use a breakpoint in the code line below to debug your script.
    return (f'Hi, {name} --you are {age} years old')

def sum1(num=0):
     try:
         if num:
         # Use a breakpoint in the code line below to debug your script.
            return int(num)+5
         else:
             return ('enter a no')
     except ValueError as err:
         return err
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
