# Dunder methods are special methods in python that start and end with double underscores.

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):              
        return self.name
    
    def __add__(self, other):
        return f"Your sum of ages are {self.age+other.age}"
    
obj = Animal("Rahul",19)
obj2 = Animal("Ram",20)
print(obj+obj2)

'''__str__() is a dunder (magic) method used to define a
human-readable string representation of an object. 
It is automatically called when print(obj) or str(obj) is used.'''

''''''
