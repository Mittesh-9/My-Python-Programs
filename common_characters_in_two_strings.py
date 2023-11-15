# Problem Description
# The program takes two strings and checks common letters in both the strings.

# Problem Solution
# 1. Enter two input strings and store it in separate variables.
# 2. Convert both of the strings into sets and find the common letters between both the sets.
# 3. Store the common letters in a list.
# 4. Use a for loop to print the letters of the list.
# 5. Exit.

s1 = input("Enter first string:")
s2 = input("Enter second string:")
a = list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)

# Program Explanation
# 1. User must enter two input strings and store it in separate variables.
# 2. Both of the strings are converted into sets and the common letters between both the sets are found using the ‘&’ operator.
# 3. These common letters are stored in a list.
# 4. A for loop is used to print the letters of the list.
