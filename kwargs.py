# learning **kwargs

def information(**kwargs):
    print("Ypur information is : ")
    for i in kwargs:
        print(f"{i} = {kwargs[i]}")


information(name = "Rahul", age = 19, Designation = "CSE AI&ML", sec = "J")