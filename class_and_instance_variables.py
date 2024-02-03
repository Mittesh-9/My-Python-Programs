# Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class. Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.

# Defining instance variables using a constructor
# Python3 program to show that the variables with a value assigned in the class declaration, are class variables and variables inside methods and constructors are instance variables.

# Class for Dog

class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed, color):

		# Instance Variable
		self.breed = breed
		self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)



# Explanation:

# A class named Dog is defined with a class variable animal set to the string “dog”. Class variables are shared by all objects of a class and can be accessed using the class name. Dog class has two instance variables breed and color. Later we are creating two objects of the Dog class and we are printing the value of both objects with a class variable named animal.

# Defining instance variables using the normal method:
# Python3 program to show that we can create
# instance variables inside methods
 
# Class for Dog

class Dog:
 
    # Class Variable
    animal = 'dog'
 
    # The init method or constructor
    def __init__(self, breed):
 
        # Instance Variable
        self.breed = breed
 
    # Adds an instance variable
    def setColor(self, color):
        self.color = color
 
    # Retrieves instance variable
    def getColor(self):
        return self.color
 
 
# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())



# Explanation:

# In this example, We have defined a class named Dog and we have created a class variable animal. We have created an instance variable breed in the constructor. The class Dog consists of two methods setColor and getColor, they are used for creating and initializing an instance variable and retrieving the value of the instance variable. We have made an object of the Dog class and we have set the instance variable value to brown and we are printing the value in the terminal.