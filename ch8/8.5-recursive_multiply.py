def recursiveMultiply(a, b, result=0):
    if b == 0:
        return result
    return recursiveMultiply(a, b-1, result+a)

print(recursiveMultiply(4, 4))