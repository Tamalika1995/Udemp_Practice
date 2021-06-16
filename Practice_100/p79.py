'''Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
and the object is in ["Hockey","Football"].
'''
import itertools
subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey","Football"]

sentence = [subject, verb, objects]
print(sentence)
n = list(itertools.product(*sentence))
for i in n:
    print(i)