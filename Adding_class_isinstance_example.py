# class Adding:
#     def __init__(self, x):
#         self.x = x
    
#     def __add__(self, z):
#         return self.x + z.x
    
# a = Adding(2)
# b = Adding(6)
# c = Adding(12)

# print(a + b + c)

class Adding:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, z):
        if isinstance(z, Adding):
            return Adding(self.x + z.x)
        elif isinstance(z, int):
            return Adding(self.x + z)
        else:
            raise TypeError("Unsupported type")

a = Adding(2)
b = Adding(6)
c = Adding(12)

print((a + b + c).x)