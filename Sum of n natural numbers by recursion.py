def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
num = int(input("Enter a number: "))
print("Sum =", sum(num))