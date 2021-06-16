import re

re1=re.compile(r'(Ha){3,5}')
print(re1.search("gfcg ha hg 'HaHaHa'").group())
print(re1.search("gfcg HaHaHaHaHa hg 'HaHaHa'").group(1))
print(re1.search("gfcg HaHaHaHaHa hg 'HaHaHa'").group(0))
re2=re.compile(r'((\w){3,5}?)')#nongreedy match
print(re2.search("gfciugh2345677789668"))
re3=re.compile(r'((\w){3,5})')#nongreedy match
print(re3.search("gfciugh2345677789668"))
re4=re.compile(r'((^\d){3,5})')#nongreedy match
print(re4.search("gfciugh2345677789668"))