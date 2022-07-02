def robotGrid(maze, x, y):
    if x == len(maze)-1 and y == len(maze[0])-1:
        return "COMPLETE!"
    
    if x < len(maze)-1 and maze[x+1][y] == 0:
        return "DOWN -> " + robotGrid(maze, x+1, y)
    
    if y < len(maze[0])-1 and maze[x][y+1] == 0:
        return "RIGHT -> " + robotGrid(maze, x, y+1)
    
    return ""

print(robotGrid(
        [
            [0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 0]
            ], 0, 0
        )
      )
