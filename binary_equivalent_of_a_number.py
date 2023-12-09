# Problem Description
# The program takes a number and finds the binary equivalent of the number without using recursion.

# Problem Solution
# 1. Take a number from the user.
# 2. Using a while loop, convert each digit into binary and append it to the list.
# 3. Reverse the list and using a for loop print the elements of the list.
# 4. Exit.

n = int(input("Enter a number: "))
a = []
while(n > 0):
    dig = n % 2
    a.append(dig)
    n = n // 2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i, end = " ")

# Program Explanation
# 1. User must enter a number.
# 3. The condition for the while loop is that the number should be greater than 0.
# 4. Otherwise, each digit is converted into binary and appended to the list.
# 5. The list is reversed and a for loop is used to print the elements of the list which is the binary equivalent of the number.