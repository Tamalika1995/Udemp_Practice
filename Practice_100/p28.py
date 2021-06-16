'''Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length,
 then the function should print all strings line by line.'''

n=input()
m=input()
l=[]
def len_check(n,m):
    if len(n)>len(m):
        l.append(n)
    elif len(n)==len(m):
        l.append(n)
        l.append(m)
    else:
        l.append(m)
    return l
print('\n'.join(len_check(n,m)))

