# Problem Description
# The program takes a string and removes the characters of odd index values in the string.

# Problem Solution
# 1. Take a string from the user and store it in a variable.
# 2. Pass the string as an argument to a function.
# 3. In the function, initialize a variable to an empty character.
# 4. Use a for loop to traverse through the string.
# 5. Use an if statement to check if the index of the string is odd or even.
# 6. If the index is odd, append the no character to the string.
# 7. Then print the modified string.
# 8. Exit.

def modify(string):
    final = ""
    for i in range(len(string)):
        if i % 2 == 0:
            final = final + string[i]
    return final

string = input("Enter string : ")
print("Modified string is : ")
print(modify(string))

# Program Explanation
# 1. User must enter a string and store it in a variable.
# 2. This string is passed as an argument to a function.
# 3. In the function, a variable is initialized with an empty character.
# 4. A for loop is used to traverse through the string.
# 5. An if statement checks if the index of the string is odd or even.
# 6. If the index is odd, the empty character variable is appended to the string thus indirectly removing the character.
# 7. Finally the modified string is printed.