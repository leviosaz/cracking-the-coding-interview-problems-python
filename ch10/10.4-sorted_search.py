def sortedSearch(listy, target):
    low = listy[0]
    high = len(listy)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        try: 
            midNum = listy[mid]
        except ValueError:
            midNum = -1
        
        if target < midNum or midNum == -1:
            high = middle - 1
        elif target > midNum:
            low = middle + 1
        else:
            return mid
    return -1 