def sortedMerge(a1, a2):
    new_array = []
    
    pointerA = 0
    pointerB = 0
    
    a1.append(float('inf'))
    a2.append(float('inf'))
    
    while len(new_array) <= len(a1) + len(a2) :
        if a1[pointerA] == a2[pointerB] and a1[pointerA] == float('inf'):
            break
        if a1[pointerA] < a2[pointerB]:
            new_array.append(a1[pointerA])
            pointerA += 1
        if a1[pointerA] > a2[pointerB]:
            new_array.append(a2[pointerB])
            pointerB += 1    
    return new_array

print(sortedMerge([1, 2, 3, 4], [-1, 5, 6, 8]))