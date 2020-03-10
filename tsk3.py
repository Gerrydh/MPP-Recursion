def prod(values):
    if len(values) == 0:
        return 0
    elif len(values) == 1:
        return values[0]
    mid = len(values) //2
    return prod(values[:mid]) * prod(values[mid:])

print(prod([1,2,3,4]))
        