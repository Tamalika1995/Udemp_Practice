import re
beginswithHello=r'^Hello'
r1=re.compile(beginswithHello)
print(r1.search('Hello hgfhgf').group())
endswithWorld=r'World$'
r2=re.compile(endswithWorld)
print(r2.search('Hello World').group())

startandend=r'^Hello(\w)*(\s)*World$'
r3=re.compile(startandend)
print(r3.search('Hello World').group())