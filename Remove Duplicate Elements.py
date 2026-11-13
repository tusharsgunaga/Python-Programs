n = [1,2,3,2,4,5,2,1,5]
#create an empty list to store the non-repeated elements
unique = []
for i in n:
    if i not in unique:
        unique.append(i)
print(unique)
    