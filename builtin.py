#1
numbers = [2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print(result)

#About lamda at the lesson
from functools import reduce
numbers = [2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)

#2
upper_count = sum(1 for char in text if 'A' <= char <= 'Z')
lower_count = sum(1 for char in text if 'a' <= char <= 'z')
print("Upper case:", upper_count)
print("Lower case:", lower_count)

#3
a=input()
x=slice(0,len(a), 1)
c=slice(len(a),0,-1)
d=slice(1)
print(a[c]+a[d]==a)

#4
import time
a=float(input("Sample input:\n"))
t=float(input())
time.sleep(t/1000)
print(f'Sample output:\nSquare root of {a} after {t} milliseconds is {a**0.5}')

#5
t1 = (True, True, True, True)
t2 = (True, True, False, True)
t3 = (True, True, True, True)
t4 = (True, True, False, True)
print(all(t1),all(t2),all(t3),all(t4))
