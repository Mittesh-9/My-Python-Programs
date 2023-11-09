# Problem Solution
# 1. Take the first two numbers of the series and the number of terms to be printed from the user.
# 2. Print the first two numbers.
# 3. Use a while loop to find the sum of the first two numbers and then proceed the fibonacci series.
# 4. Print the fibonacci series till n-2 is greater than 0.
# 5. Exit.

a = int(input("Enter the first number of the series "))
b = int(input("Enter the second number of the series "))

n = int(input("Enter the number of terms needed "))

print(a,b, end = " ")
while(n-2):
    c = a + b
    a = b
    b = c
    print(c, end = " ")
    n = n - 1

# Program Explanation
# 1. User must enter the first two numbers of the series and the number of terms to be printed.
# 2. The first two terms are printed outside the while loop.
# 3. A while loop is used to find the sum of the first two terms and proceed the series by interchanging the variables.
# 4. The value of n is decremented.
# 5. The fibonacci series is printed till n-2 is greater than 0.
