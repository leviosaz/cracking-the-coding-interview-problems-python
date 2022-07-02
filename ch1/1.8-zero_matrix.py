def zeroMatrix(matrix):
    coordinates = []
    
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == 0:
                coordinates.append([x, y])
    
    for x in coordinates:
        # sort the x
        matrix[x[0]] = [0 for x in range(len(matrix[x[0]]))]
        
        # sort the y
        for r in range(len(matrix)):
            matrix[r][x[1]] = 0
    
    return matrix
    
print(zeroMatrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))