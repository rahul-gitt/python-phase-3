# Basic use case of decorator

def decorate(func):
    def wrapper():
        print("I am print before the function return.")
        func()
        print("I am print after the function.")
    return wrapper


@decorate
def hello():
    print("Hello my name is Rahul Mondal")

hello()