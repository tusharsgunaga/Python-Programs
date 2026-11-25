numbers = [12, 7, 18, 5, 20, 9, 14, 3]
result = list(filter(lambda x: True if x % 2 == 0 else False, numbers))
print(result)