n = "engineering"
d = {}
for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    if d[i] == max(d.values()):
        print(i)