l = []

def convert(b):
    if(b==0):
        return l
    dig = b % 2
    l.append(dig)
    convert(b//2)
a = int(input("Enter a number: "))
convert(a)
l.reverse()
print("Binary equivalent:")
for i in l:
    print i,

# Program Explanation
# 1. A recursive function is defined which takes a number as the argument.
# 2. A number is taken from the user and passed as an argument to a recursive function.
# 3. In the function, the base condition is that if the number is zero, the formed list is returned.
# 4. Otherwise, each digit is converted into binary and appended to the list.
# 5. The list is reversed and a for loop is used to print the elements of the list.
