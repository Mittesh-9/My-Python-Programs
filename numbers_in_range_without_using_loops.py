# Problem Description
# The program takes in the upper limit and prints all numbers within the given range using recursive function.

# Problem Solution
# 1. Define a recursive function.
# 2. Define a base case for that function that the number should be greater than zero.
# 3. If number is greater than 0, call the function again with the argument as the number minus 1.
# 4. Print the number.
# 5. Exit.

def printno(upper):
    if(upper > 0):
        printno(upper-1)
        print(upper)

upper = int(input("Enter upper linit :"))
printno(upper)

# Program Explanation
# 1. User must enter the upper limit of the range.
# 2. This value is passed as an argument for the recursive function.
# 3. The base case for the recursive function is that number should always be greater than 0.
# 4. If number is greater than 0, function is called again with the argument as the number minus 1.
# 5. The number is printed.
# 6. The recursion continues until the number becomes lesser than 0.
