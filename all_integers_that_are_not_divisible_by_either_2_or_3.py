# Problem Description
# The program prints all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50.

# Problem Solution
# 1. Use a for-loop ranging from 0 to 51.
# 2. Then use an if statement to check if the number isn’t divisible by both 2 and 3.
# 3. Print the numbers satisfying the condition.
# 4. Exit.

for i in range(0, 51):
    if (i % 2 != 0 & i % 3 != 0):
        print(i)

# Program Explanation
# 1. The for loop ranges from 0 to 50 (as 51 isn’t exclusive).
# 2. The expression within the if-statement checks if the remainder obtained when the number divided by 2 and 3 is one or not.
# 3. If the remainder isn’t equal to 0, the number isn’t divisible by either 2 and 3.
# 4. The number satisfying the condition is printed.