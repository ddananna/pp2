import re

with open("row.txt", "r", encoding="utf-8") as fr:
    reading = fr.readlines()
s = ''.join(reading)

#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
p = re.compile('ab*')
m = p.findall(s)
if m:
    print(m)
else:
    print("ERROR")

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
p = re.compile('ab{2,3}')
m = p.findall(s)
if m:
    print(m)
else:
    print("ERROR")

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.
p = re.compile('[a-z]+_[a-z]+')
m = p.findall(s)
if m:
    print(m)
else:
    print("ERROR")

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
p = re.compile('[A-Z][a-z]+')
m = p.findall(s)
if m:
    print(m)
else:
    print("ERROR")

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
p = re.compile(r'a[\w.]+b')
m = p.findall(s)
if m:
    print(m)
else:
    print("ERROR")

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
p = re.sub(r'[ ,.]', ':', s)
print(p)

#7 Write a python program to convert snake case string to camel case string.
def toCamel(snake):
    return snake.group(1).upper()

p = re.sub(r'_([a-z])', toCamel, s)
print(p)

#8 Write a Python program to split a string at uppercase letters.
def splits(words):
    words = re.findall(r'[A-Z][a-z]*', s)
    return words

a = ' '.join(splits(s)) 
print(a)

#9 Write a Python program to insert spaces between words starting with capital letters.
def spaces(word):
    return ' ' + word.group(0)

p = re.sub(r'[A-Z]', spaces, s)
print(p)

#10 Write a Python program to convert a given camel case string to snake case.
def to_snake(camel):
    return '_' + camel.group(0).lower()

p = re.sub(r'[A-Z][a-z]', to_snake, s)
print(p)
