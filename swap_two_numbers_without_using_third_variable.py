# Problem Description
# The program takes both the values from the user and swaps them without using temporary variable.

# Problem Solution
# 1. Take the values of both the elements from the user.
# 2. Store the values in separate variables.
# 3. Add both the variables and store it in the first variable.
# 4. Subtract the second variable from the first and store it in the second variable.
# 5. Then, subtract the first variable from the second variable and store it in the first variable.
# 6. Print the swapped values.
# 7. Exit.

a = int(input("Enter value of first variable: "))
b = int(input("Enter value of second variable: "))
a = a + b
b = a - b
a = a - b
print("a is:",a," b is:",b)

# Program Explanation
# 1. User must first enter the values for both the elements.
# 2. The first element is assigned the sum of the first two elements.
# 3. Second element is assigned the difference between the sum in the first variable and the second variable, which is basically the first element.
# 4. Later the first element is assigned the difference between the sum in the variable and the second variable, which is the second element.
# 5. Then the swapped values are printed.
