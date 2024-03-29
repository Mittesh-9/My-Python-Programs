# Problem Description
# The program takes the elements of the list one by one and displays the average of the elements of the list.

# Problem Solution
# 1. Take the number of elements to be stored in the list as input.
# 2. Use a for loop to input elements into the list.
# 3. Calculate the total sum of elements in the list.
# 4. Divide the sum by total number of elements in the list.
# 5. Exit.

number_of_elements = int(input("Enter the number of elements to be inserted : "))
a = []
for i in range(0, n):
    element =int(input("Enter element : "))
    a.append(element)
avg = sum(a) / n
print("Average of elements in the list", round(avg, 2))

# Program Explanation
# 1. User must first enter the number of elements which is stored in the variable n.
# 2. The value of I ranges from 0 to the number of elements and is incremented each time after the body of the loop is executed.
# 3. Then, the element that the user enters is stored in the variable elem.
# 4. a.append(elem) appends the element to the list.
# 5. Now the value of i is incremented to 2.
# 6. The new value entered by the user for the next loop iteration is now stored in elem which is appended to the list.
# 7. The loop runs till the value of i reaches n.
# 8. sum(a) gives the total sum of all the elements in the list and dividing it by the total number of elements gives the average of elements in the list.
# 9. round(avg,2) rounds the average upto 2 decimal places.
# 10. Then the average is printed after rounding.
