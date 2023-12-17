# Problem Description
# The program takes two strings and displays which letters are in the first string but not in the second string.

# Problem Solution
# 1. Enter two input strings and store it in separate variables.
# 2. Convert both of the strings into sets and find which letters are present in the first string but not in the second string.
# 3. Store the letters in a list.
# 4. Use a for loop to print the letters of the list.
# 5. Exit.

s1 = input("Enter first string:")
s2 = input("Enter second string:")
a = list(set(s1)-set(s2))
print("The letters are:")
for i in a:
    print(i)

# 1. User must enter two input strings and store it in separate variables.
# 2. Both of the strings are converted into sets and the letters which are in the first string but not in the second string are found using the ‘-‘ operator.
# 3. These letters are stored in a list.
# 4. A for loop is used to print the letters of the list.
