'''All of these comprehension are used to create List,Dictionary,Set.
 But we don't have to use multiple lines of code for loops and If-Else statement'''
    
# List comprehension

l = [i for i in range(1,21) if i%2 == 0 ]
print(l) #Print even numbers only

# Dictionary comprehension

d = {i : i**2 for i in range(1,11)}
print(d)    # print key valus of the dictionary

# Set comprehension

s = {x*x for x in range(1,20)}
print(s)    # print the set