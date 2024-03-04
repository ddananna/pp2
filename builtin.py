# Task 1: Multiply all numbers in a list
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

# Task 2: Calculate the number of upper case and lower case letters in a string
text = "Hello, World!"
upper_count = sum(1 for char in text if 'A' <= char <= 'Z')
lower_count = sum(1 for char in text if 'a' <= char <= 'z')
print("Upper case:", upper_count)
print("Lower case:", lower_count)

# Task 3: Check if a string is palindrome or not
text = "radar"
is_palindrome = text == text[::-1]
print("Palindrome" if is_palindrome else "Not a palindrome")

# Task 4: Invoke square root function after a specific milliseconds
def square_root(number):
    return number ** 0.5

number = 25100
milliseconds = 2123
# Sleep function without using time module
start_time = sum([1 for i in range(milliseconds)])  # Approximate sleep
end_time = start_time + 1
while start_time < end_time:
    start_time += 1
# End of sleep function
print(f"Square root of {number} after {milliseconds} milliseconds is {square_root(number)}")
