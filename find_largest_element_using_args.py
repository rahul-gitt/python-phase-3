# Find largest element using args

def num(*args):
    large = args[0]
    for i in args:
        if i > large:
            large = i

    print(f"The largest number is : {large}")

num(12,35,67,0,67,45,65)