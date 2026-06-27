# Map()

#map() applies a function to every element of an iterable and returns a map object.

number = [1,2,3,4,5,6,7,8,9,10]

square = list(map(lambda x: x*2,number))

print(square)