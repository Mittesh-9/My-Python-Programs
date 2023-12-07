# Problem Description
# The program reads the height in centimeters and then converts the height to feet and inches.

# Problem Solution
# 1. Take the height in centimeters and store it in a variable.
# 2. Convert the height in centimeters into inches and feet.
# 3. Print the length in inches and feet.
# 4. Exit.

cm = int(input("Enter the height in centimeters : "))
inches = 0.394 * cm
feet = 0.0328 * cm
print("The length in inches",round(inches, 2))
print("The length in feet",round(feet, 2))

# Program Explanation
# 1. User must enter the height in centimeters.
# 2. The height in centimeters is multiplied by 0.394 and stored in another variable which now contains the height in inches.
# 3. The height in centimeters is multiplied by 0.0328 and stored in another variable which now contains the height in feet.
# 4. The converted height in inches and feet is printed.
