number = int(input("Enter a number : "))
reversed_number = int(str(number)[::-1])
print("Reversed number :", reversed_number)

# Program Explanation
# 1. The user is prompted to enter a number.
# 2. The input number is converted to a string using str(number).
# 3. The string representation of the number is reversed using slicing with [::-1].
# 4. The reversed string is converted back to an integer using int().
# 5. The reversed number is stored in the variable reversed_number.
# 6. The reversed number is printed as the output.

# Time Complexity: O(n)
# The time complexity of the program is O(n), where n is the number of digits in the input number. This is because the program iterates through each digit of the number once to reverse it.

# Space Complexity: O(n)
# The space complexity is also O(n) because the reversed_number variable stores the reversed number, which requires space proportional to the number of digits in the input number.
