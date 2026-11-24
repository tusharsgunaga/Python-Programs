from functools import reduce
n = [4, 7, 2, 9, 4]
result = reduce(lambda a,b: a * 10 + b, n)
print("The number is: ", result)