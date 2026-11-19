s = "Python programming is very interesting"
long = ""
for i in s.split():
    if len(i) > len(long):
        long = i
print(long)