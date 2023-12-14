# Problem Description
# The program takes in the number of elements and generates random numbers from 1 to 20 and appends them to the list.

# Problem Solution
# 1. Import the random module into the program.
# 2. Take the number of elements from the user.
# 3. Use a for loop, random.randint() is used to generate random numbers which are them appending to a list.
# 4. Then print the randomised list.
# 4. Exit.

import random
a = []
n = int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)

# Program Explanation
# 1. The random module is imported into the program.
# 2. User must enter the number of elements from the user.
# 3. Using a for loop, random.randint() is used to generate random numbers which are then appended to a list.
# 4. The arguments given inside the random.randint() function are used to specify the range to print the randomized numbers within.
# 5. Then the randomized list is printed.
