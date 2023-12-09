# In this approach, we will divide the number by 10 and add the remainder to the sum.

n = int(input("Enter number: "))
rev = 0
while(n > 0):
    dig = n % 10
    rev=rev * 10 + dig
    n = n // 10
print("Reverse of the number: ",rev)

# Program Explanation
# 1. User enters a number. Entered number is stored in the variable n.
# 2. A variable rev is initialized to 0, which will store the reversed number.
# 3. Using a while loop, the digits of the number are extracted and added to rev in reverse order.
# 4. The number is divided by 10 in each iteration to remove the last digit.
# 5. The reversed number is displayed as output.

# Time Complexity: O(log n)
# The time complexity of the program is O(log n), where n is the input number. This is because the number of iterations in the while loop is proportional to the number of digits in the input number.

# Space Complexity: O(1)
# The space complexity of the program is O(1) since it uses a constant amount of additional space to store the variables n, rev, and dig. The space required does not depend on the input size.
