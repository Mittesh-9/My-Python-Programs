# Problem Description
# The program takes a number and searches the number of times the particular number occurs in a list.

# Problem Solution
# 1. Take in the number of elements for the first list and store it in a variable.
# 2. Take in the elements of the list one by one.
# 3. Then take in the number to be searched in the list.
# 4. Use a for loop to traverse through the elements in the list and increment the count variable.
# 5. Display the value of the count variable which contains the number of times a particular number occurs in a list.
# 6. Exit.

a = []
n = int(input("Enter number of elements : "))

for i in range(1, n + 1):
    b = int(input("Enter element : "))
    a.append(b)

k = 0

num = int(input("Enter the number to be counted : "))
for j in a :
    if (j == num):
        k = k + 1

print("Number of times",num,"appears is",k)

# Program Explanation
# 1. User must enter the number of elements for the first list and store it in a variable.
# 2. User must then enter the elements of the list one by one using a for loop and store it in a list.
# 3. User must also enter the number to be search the list for.
# 4. A for loop is used to traverse through the elements in the list and an if statement is used to count a particular number.
# 5. The total count of a particular number in the list is printed.