l = [12, 7, 5, 8, 10, 3, 6]
even = 0
odd = 0
for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers are: ", even)
print("Number of odd numbers are: ",odd)