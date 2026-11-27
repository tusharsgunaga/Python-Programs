
names = ["Tushar", "Amey", "Dhruva", "Tejas"]
marks = [98, 47, 96, 23]

data = list(zip(names, marks))

result = list(map(lambda x: (x[0], x[1] + 5), filter(lambda x: x[1] >= 50, data)))

print(result)
