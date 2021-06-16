'''Please raise a RuntimeError exception.'''

try:
    print(9/0)
except:
    raise RuntimeError('something wrong')