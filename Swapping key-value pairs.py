data = [
    {'a': 1, 'b': 'x'},
    {'c': 2, 'd': [1, 2]}
]

def swap(d):
    return {
        (v if isinstance(v, (str, int)) else k):
        (k if isinstance(v, (str, int)) else v)
        for k, v in d.items()
    }

result = list(map(swap, data))
print(result)