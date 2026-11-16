l = [1,2,3,4,2,5,1,4,3,1]
unique = []
for i in l:
    if i not in unique:
        unique.append(i)
print("The updated list of non-repeated elements is: ", unique)