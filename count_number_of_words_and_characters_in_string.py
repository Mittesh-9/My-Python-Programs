# Problem Description
# The program takes a string and calculates the number of words and characters present in the string.

# Problem Solution
# 1. Take a string from the user and store it in a variable.
# 2. Initialize the character count variable to 0 and the word count variable to 1.
# 3. Use a for loop to traverse through the characters in the string and increment the character count variable each time.
# 4. Increment the word count variable only if a space is encountered.
# 5. Print the total count of the characters and words in the string.
# 6. Exit.

string = input("Enter string : ")
char = 0
word = 1
for i in string:
    char = char + 1
    if(i == ' '):
        word = word + 1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

# Program Explanation
# 1. User must enter a string and store it in a variable.
# 2. The character count variable is initialized to zero and the word count variable is initialized to 1 (to account for the first word).
# 3. The for loop is used to traverse through the characters in the string.
# 4. The character count is incremented each time a character is encountered and the word count is incremented only when a space is encountered.
# 6. The total count of characters and the words in the string is printed.
