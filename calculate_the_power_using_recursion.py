# Problem Description
# The program takes a base and a power and finds the power of the base using recursion.

# Problem Solution
# 1. Take the base and exponential value from the user.
# 2. Pass the numbers as arguments to a recursive function to find the power of the number.
# 3. Give the base condition that if the exponential power is equal to 1, return the base number.
# 4. If the exponential power isn’t equal to 1, return the base number multiplied with the power function called recursively with the arguments as the base and power minus 1.
# 5. Print the final result.
# 6. Exit.

def power(base, exp):
    if(exp == 1):
        return(base)
    if(exp != 1):
        return(base * power(base, exp - 1))
base = int(input("Enter base : "))
exp = int(input("Enter exponential value : "))
print("Result :",power(base,exp))

# Program Explanation
# 1. User must enter the base and exponential value.
# 2. The numbers are passed as arguments to a recursive function to find the power of the number.
# 3. The base condition is given that if the exponential power is equal to 1, the base number is returned.
# 4. If the exponential power isn’t equal to 1, the base number multiplied with the power function is called recursively with the arguments as the base and power minus 1.
# 5. The final result is printed.