# Problem Description
# The program takes a string and calculates the length of the string without using library functions.

# Problem Solution
# 1. Take a string from the user and store it in a variable.
# 2. Initialize a count variable to 0.
# 3. Use a for loop to traverse through the characters in the string and increment the count variable each time.
# 4. Print the total count of the variable.
# 5. Exit.

string = input("Enter string : ")
count = 0
for i in string:
      count = count + 1
print("Length of the string is : ")
print(count)

# Program Explanation
# 1. User must enter a string and store it in a variable.
# 2. The count variable is initialized to zero.
# 3. The for loop is used to traverse through the characters in the string.
# 4. The count is incremented each time a character is encountered.
# 5. The total count of characters in the string which is the length of the string is printed.
