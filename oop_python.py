
# Python OOP - Property Decorators - Getters, Setters, and Deleters.

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

empl_1 = Employee('mittesh', 'waghule')

empl_1.fullname = 'rach dsouza'

print(empl_1.first)
print(empl_1.email)
print(empl_1.fullname)

del empl_1.fullname

print(empl_1.first)
print(empl_1.email)
print(empl_1.fullname)