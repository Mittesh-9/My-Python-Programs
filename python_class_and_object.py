# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Creating a class
class MyClass:
    a = 1

# Create object
# Created an object named o1, and print the value of x:
o1 = MyClass()
print(o1.a)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Mittesh", 22)

print(p1.name)
print(p1.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Mithilesh", 22)

print(p1)

# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("mitt", 18)

print(p1)