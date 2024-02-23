import math

# Task 1: Convert degree to radian
degree = 15
radian = degree * math.pi / 180
print("Input degree:", degree)
print("Output radian:", round(radian, 6))

# Task 2: Calculate the area of a trapezoid
height = 5
base1 = 5
base2 = 6
area_trapezoid = 0.5 * (base1 + base2) * height
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area_trapezoid)

# Task 3: Calculate the area of a regular polygon
num_sides = 4
side_length = 25
area_polygon = num_sides * side_length ** 2 / (4 * math.tan(math.pi / num_sides))
print("Input number of sides:", num_sides)
print("Input the length of a side:", side_length)
print("The area of the polygon is:", area_polygon)

# Task 4: Calculate the area of a parallelogram
base_length = 5
height_parallelogram = 6
area_parallelogram = base_length * height_parallelogram
print("Length of base:", base_length)
print("Height of parallelogram:", height_parallelogram)
print("Expected Output:", area_parallelogram)
