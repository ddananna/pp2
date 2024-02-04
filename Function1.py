#1
def ouncetogramm(gramm):
    ounce = gramm * 29.3495231
    return ounce
g = int(input())
o = ouncetogramm(g)
print(f"{o} ounces")

#2
def c(f):
    cel = (5/9) * (f - 32)
    return cel
ff = int(input())
cc = c(ff)
print(f"{cc} celcius")

#3
def solve(numheads,numlegs):
    c = numheads -(numlegs - (numheads * 2))/2
    r = (numlegs - (2 * numheads))/2
    return c ,r 
h = int(input())
l = int(input())
ch ,ra = solve(h,l)
print(f"{ch} chickens, {ra} rabbits")

#4
def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
            if num % i == 0:
                cnt = cnt + 1
    return cnt == 2

result2 = [x for x in map(int, input().split()) if isPrime(x)]#comprehension of list
print(result2)

#5
from itertools import permutations
def permutationation():
    perm = input()
    perms = permutations(perm)
    for i in perms:
        print(''.join(i))
permutationation()

#6
def reverse(s):
    word = s.split()
    revse = ' '.join(word[::-1])
    return revse
s = input()
revse = reverse(s)
print(revse)

#7
def has_33():
    num = input()
    nums = list(map(int,num.split()))
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            print("True")
            return True
    print("False")
has_33()  

#8
def spy_game(nums):
    cnt0 = 0
    dz = False
    for num in nums:
        if num == 0:
            cnt0 = cnt0+1
            if cnt0 >= 2:
                dz = True
        elif num == 7 and dz:
            return True
    return False
print(spy_game(list(map(int,input().split()))))      

#9
import math
def sphere(rad):
    Area = 4 * math.pi * rad ** 2
    print(Area)
r = int(input())
sphere(r)    

#10
def unique(listo):
    listo.sort()
    for i in range(len(listo)-1,0,-1):
        if(listo[i]==l[i-1]):
            listo.remove(l[i])
    print(listo)
unique(list(input("list: ").split()))

#11
def palind(word):
    revwo = word[::-1]
    if revwo == word:
        print("Word is palindrome")
    else:
        print("Word is not palidrome")
wrod = input()
palind(wrod) 

#12
def histogram(his):
    for i in range(len(his)):
        print("*"*his[i])
histogram(list(map(int(input().split()))))

#13
import random
def guess(gu):
    guess = 0
    guessed = False
    print(f"Well,{gu},I am thinking of a number between 1 and 20.")
    num = random.randint(1,20)
    while(guessed == False):
        guess += 1
        gn = int(input("Take a guess.\n"))
        if gn == num:
            print(f"Good job,{gu}! You guessed my number in {guess} guesses!")
            guessed = True
        elif gn < num:
            print("Your guess is too low.")
        elif gn > num:
            print("Your guess is too high.")
guess(input("Hello! What is your name?\n"))
