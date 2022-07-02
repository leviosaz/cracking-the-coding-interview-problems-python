def uniqueString(string):
    hashmap = {}
    
    for x in string:
        if hashmap.get(x):
            return False
        hashmap[x] = 1
    return True

print(uniqueString("ab"))