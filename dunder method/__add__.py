# Learing __add__ dunder method

class Boys :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Your name is {self.name}"
    
    def __add__(self, other):
        sum = 0 
        for i in other:
            sum = sum+ i.age
        return f"The sum of ages are {self.age+sum}"

obj = Boys("Rahul",19)
obj2 = Boys("Dev",23)
obj3 = Boys("Debu",20)

print(obj + (obj2,obj3))

print(obj)
print(obj2)
print(obj3)