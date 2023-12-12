# Problem Description
# The program takes a string and counts the number of lowercase letters and uppercase letters in the string.

# Problem Solution
# 1. Take a string from the user and store it in a variable.
# 2. Initialize the two count variables to 0.
# 3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a lowercase character is encountered and increment the second count variable each time a uppercase character is encountered.
# 4. Print the total count of both the variables.
# 5. Exit.

string = input("Enter string :")
count1 = 0
count2 = 0
for i in string:
      if(i.islower()):
            count1 = count1 + 1
      elif(i.isupper()):
            count2 = count2 + 1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)

# Program Explanation
# 1. User must enter a string and store it in a variable.
# 2. Both the count variables are initialized to zero.
# 3. The for loop is used to traverse through the characters in the string.
# 4. The first count variable is incremented each time a lowercase character is encountered and the second count variable is incremented each time a uppercase character is encountered.
# 5. The total count of lowercase characters and uppercase characters in the string are printed.
