# Problem Description
# The program takes a string and checks if it is a pangram or not.

# Problem Solution
# 1. Take a string from the user and store it in a variable.
# 2. Pass the string as an argument to a function.
# 3. In the function, form two sets- one of all lower case letters and one of the letters in the string.
# 4. Subtract these both sets and check if it is equal to an empty set.
# 5. Print the final result.
# 6. Exit.

from string import ascii_lowercase as asc_lwr

def check(s):
    return set(asc_lwr) - set(s.lower()) == set([])

string = input("Enter string ")

if(check(string) == True):
    print("The string is a panagram")
else:
    print("The string isn't a panagram")

#Program Explanation
# 1. User must enter a string and store it in a variable.
# 2. The string is passed as an argument to a function.
# 3. In the function, two sets are formed- one for all lower case letters and one for the letters in the string.
# 4. The two sets are subtracted and if it is an empty set, the string is a pangram.
# 6. The final result is printed.