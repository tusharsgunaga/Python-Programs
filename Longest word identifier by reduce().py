from functools import reduce
s =  ["recursion", "backtracking", "tree", "algorithm", "graph"]
longest = []
result = reduce(lambda m,n: m if len(m) > len(n) else n, s)
print(result)