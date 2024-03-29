# Problem Description
# The program takes a number n and prints an identity matrix of the desired size.

# Problem Solution
# 1. Take a value from the user and store it in a variable n.
# 2. Use two for loop where the value of j ranges between the values of 0 and n-1 and value of i also ranges between 0 and n-1.
# 3. Print the value of 1 when i is equal to j and 0 otherwise.
# 4. Exit.

n = int(input("Enter a number : "))
for i in range(0, n):
    for j in range(0, n):
        if(i == j):
            print("1",sep = " ",end = " ")
        else:
            print("0",sep = " ",end = " ")
    print()

# Program Explanation
# 1. User must first enter the value and store it in a variable n.
# 2. The outer for loop enables j to range between 1 and n-1 (as n is not included) while the inner for loop also enables i to range between 1 and n-1.
# 3. For each iteration, the value of 1 is printed if i is equal to j and value of 0 is printed otherwise.
# 4. The sep and end parameters of the print function help in formatting and print() allows values to printed in a new line for each iteration of the outer for loop.
