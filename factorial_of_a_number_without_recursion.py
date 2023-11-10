# Problem Description
# The program takes a number and finds the factorial of that number without using recursion.

# Problem Solution
# 1. Take a number from the user.
# 2. Initialize a factorial variable to 1.
# 3. Use a while loop to multiply the number to the factorial variable and then decrement the number.
# 4. Continue this till the value of the number is greater than 0.
# 5. Print the factorial of the number.
# 6. Exit.

n = int(input('Enter number : '))
fact = 1
while(n > 0):
    fact = fact * n
    n = n - 1
print("Factorial of the number is : ")
print(fact)

# Program Explanation
# 1. User must enter a number.
# 2. A factorial variable is initialized to 1.
# 3. A while loop is used to multiply the number to the factorial variable and then the number is decremented each time.
# 4. This continues till the value of the number is greater than 0.
# 5. The factorial of the number is printed.
