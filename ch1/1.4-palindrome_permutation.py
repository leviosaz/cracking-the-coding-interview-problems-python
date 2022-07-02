def palindromePermutation(string):
    
    hashtable = {}
    
    for x in string:
        if hashtable.get(x) == 1:
            del hashtable[x]
            continue
        hashtable[x] = 1
    
    
    if len(hashtable.keys()) > 1:
        return False
    return True

print(palindromePermutation("tacocatt"))
print(palindromePermutation("tacocat"))
            
            