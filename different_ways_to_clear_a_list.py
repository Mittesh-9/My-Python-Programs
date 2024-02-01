# There are many ways of clearing the list through methods of different constructs offered by Python language. Let’s try to understand each of the methods one by one.

# 1) Using clear()

GEEK = [6, 0, 4, 1]
print('GEEK before clear:', GEEK)

# Clearing list
GEEK.clear()
print('GEEK after clear:', GEEK)

# 2) Reinitializing the list

list1 = [1, 2, 3]

# Printing list2 before deleting
print("List1 before deleting is : "
	+ str(list1))

# deleting list using reinitialization
list1 = []

# Printing list2 after reinitialization
print("List1 after clearing using reinitialization : "
	+ str(list1))

# 3) Using “*= 0”

# Initializing lists
list1 = [1, 2, 3]

# Printing list2 before deleting
print("List1 before clearing is : "
	+ str(list1))

list1*=0
# Printing list2 after reinitialization
print("List1 after clearing using *=0 : "
	+ str(list1))

# 4) Using del

list1 = [1, 2, 3]
list2 = [5, 6, 7]

# Printing list1 before deleting
print("List1 before deleting is : " + str(list1))

# deleting list1 using del
del list1[:]
print("List1 after clearing using del : " + str(list1))


# Printing list2 before deleting
print("List2 before deleting is : " + str(list2))

# deleting list using del
del list2[:]
print("List2 after clearing using del : " + str(list2))

# 5) Using pop() method

list1 = [1, 2, 3]

# Printing list1 before deleting
print("List1 before deleting is : " + str(list1))

# deleting list1
while(len(list1) != 0):
	list1.pop()
print("List1 after clearing using del : " + str(list1))

# 6) Using slicing

# Initializing list
lst = [1, 2, 3, 4, 5]

print("List before clearing: ",lst)
# Clearing list using slicing
lst = lst[:0]
print("List after clearing using Slicing: ",lst)
