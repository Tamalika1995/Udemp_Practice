import re
import pprint as p

messge='this is my no 871-098-4567 or 678-098-0987'
phnoregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phnoregex.search(messge).group()
moall=phnoregex.findall(messge)
print(mo)
p.pprint(moall)
print('new'.center(18,'*'))
phnoregex1=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1=phnoregex1.search(messge).group()
mo2=phnoregex1.search(messge).group(1)
mo3=phnoregex1.search(messge).group(2)
moall1=phnoregex1.findall(messge)
print(mo1)
print(mo2)
print(mo3)
p.pprint(moall1)
