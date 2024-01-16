# by using a temporary variable

# x = 5
# y = 10

# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# creating a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# without using temporary variable

x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)
