c =  ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r','l','d']
vowels = list(filter(lambda v: True if v in ['a','e','i','o','u'] else False, c))
print("The vowels are: ",vowels)