# learning *args

def addition(*args):
    sum = 0
    for i in args:
        sum = sum+i

    print(f"The total is : {sum}")


addition(12,374,45,76,99,34,232,565,3)
