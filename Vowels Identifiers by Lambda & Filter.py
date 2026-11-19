c = ['h','e','l','l','o','w','o','r','l','d']

vowels = list(filter(lambda i: True if i in ['a','e','i','o','u'] else False, c))

print("The vowels are: ", vowels)