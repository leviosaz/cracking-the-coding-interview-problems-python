def rotateMatrix(matrix):
    newMatrix = []
    
    for x in range(len(matrix)):
        tmpRow = []
        for y in range(len(matrix)):
            tmpRow.append(matrix[y][x])
        newMatrix.append(tmpRow)

    return newMatrix

print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))