n = [2,7,11,15]
target = 9
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == target:
            print([i,j])