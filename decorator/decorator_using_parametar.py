# leat's learn decoratr using parametar

def decorate(func):
    def wrapper(a,b):
        print("Addition of your numbers are ->")
        func(a,b)
        print("Thank you")
    return wrapper

@decorate
def addition(a,b):
    print(f"The total is : {a+b}")

addition(45,18)
