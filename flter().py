#filter() → Selects elements based on a condition.

number = [23,34,56,98,2,54,65,76,92,24]

result = filter(lambda x: True if x%2 ==0 else False,number)
print(list(result))