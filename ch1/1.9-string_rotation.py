def stringRotation(a, b):    
    if len(a) != len(b):
        return False
    
    for x in range(len(a)):
        b = b[-1] + b[:-1]
        if b == a:
            return True 
    return False

print(stringRotation("waterbottle", "erbottlewat"))