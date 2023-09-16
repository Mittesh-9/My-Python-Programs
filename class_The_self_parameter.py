class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("Hello my name is " + abc.name)
        print("My age is" ,abc.age)

p1 = Person("Mittesh", 22)
p1.myfunc()


# Modify Object Properties
# You can modify properties on objects like this:
p1.age = 25

# Delete Object Properties
# You can delete properties on objects by using the del keyword:
del p1.age

# Delete Objects
# You can delete objects by using the del keyword:
del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
    pass