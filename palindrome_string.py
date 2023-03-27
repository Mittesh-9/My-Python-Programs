# The code first prompts the user to enter a string, removes any whitespaces and converts the string to lowercase. It then checks if the string is equal to its reverse using the [::-1] slicing technique, which reverses the string. If the string is equal to its reverse, the code prints a message saying that the string is a palindrome, otherwise it prints a message saying that the string is not a palindrome.

string = input("Enter a string: ")

# remove whitespaces and convert to lowercase
string = string.replace(" ", "").lower()

# check if the string is equal to its reverse
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
