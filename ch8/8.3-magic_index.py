def magicIndex(array, start, end):
    if end < start:
        return "No magic index was found."
        
    mid = int((start + end)/2)
    
    # Base case for magicIndex
    print(f"{mid} and {array[mid]}")
    if mid == array[mid]:
        return f"The index {mid} has the value {array[mid]}"

    # Recursive portion
    if array[mid] > mid:
        return magicIndex(array, start, mid-1)
    
    if mid > array[mid]:
        return magicIndex(array, mid+1, end)
    
print(magicIndex([-2, 1, 3, 4, 5, 6], 0, 5))