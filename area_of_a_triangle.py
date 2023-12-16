# Problem Description
# The program takes three sides of a triangle and prints the area formed by all three sides.

# Problem Solution
# 1. Take in all the three sides of the triangle and store it in three separate variables.
# 2. Then using the Heron’s formula, compute the area of the triangle.
# 3. Print the area of the triangle.
# 4. Exit

import math
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ",round(area,2))

# Program Explanation
# 1. User must enter all three numbers and store it in separate variables.
# 2. First the value of s is found out which is equal to (a+b+c)/2
# 3. Then the Heron’s formula is applied to determine the area of the triangle formed by all three sides.
# 4. Then the area of the triangle is printed.
