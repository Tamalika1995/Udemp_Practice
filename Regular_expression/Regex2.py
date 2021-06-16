import re
m=r'Bat(man|mobile|copter|gun)'
re1=re.compile(m)
print(re1.search("Batgun").group())
print(re1.search("Batcopter hgfh Batmobile").group(1))
print(re1.search("Batcopter hgfh Batmobile").group(0))
print(re1.findall("Batcopter hgfh Batmobile"))
print(re1.search("Batcopte"))

