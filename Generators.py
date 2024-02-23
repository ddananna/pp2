# Task 1: Generator for squares of numbers up to N
def square_generator(N):
    for i in range(N):
        yield i**2

# Task 2: Program to print even numbers between 0 and n
n = int(input())
even_numbers = (str(i) for i in range(n+1) if i % 2 == 0)
print(','.join(even_numbers))

# Task 3: Function with generator for numbers divisible by 3 and 4 in range 0 to n
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Task 4: Generator to yield squares of numbers from a to b
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

# Task 5: Generator to return numbers from n down to 0
def numbers_down_to_zero(n):
    for i in range(n, -1, -1):
        yield i

# Testing Task 4 with a "for" loop
for square in squares(1, 5):
    print(square)
