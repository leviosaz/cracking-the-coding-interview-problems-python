def searchInRotatedArray(arr, element):
    length = len(arr)
    mid = length//2
    counter = 1
    
    while arr[mid] != element and counter * 2 < length:
        if element > arr[mid]:
            mid = mid + (length // (2* counter))
            mid = mid % length
            counter += 1
        if element < arr[mid]:
            mid = mid - (length // (2 * counter)) 
            mid = mid % length
            counter += 1

    if arr[mid] == element:
        return mid
    return None
    
print(searchInRotatedArray([15, 16, 19, 20, 25, 1, 3, 4, 5], 5))