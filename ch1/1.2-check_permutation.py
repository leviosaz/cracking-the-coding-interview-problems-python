from collections import Counter

def checkPermutation(a, b):    
    if len(a) != len(b):
        return False
    
    hashmap = Counter(a)
    
    for x in b:
        if not hashmap.get(x): # if it's 0 or None, it'll return False
            return False
            continue
        hashmap[x] = hashmap[x]-1
        
    return True
    

print(checkPermutation("cat", "tdac"))