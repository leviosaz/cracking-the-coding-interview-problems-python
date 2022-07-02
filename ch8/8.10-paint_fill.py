def paintFill(map, x, y, color, newColor):
    if x > 0 and map[x-1][y] == color:
        map[x-1][y] = newColor
        x -= 1
    elif x < len(map) and map[x+1][y] == color:
        map[x+1][y] = newColor
        x += 1
    elif y > 0 and map[x][y-1] == color:
        map[x][y-1] = newColor
        y -= 1
    elif y < len(map[0]) and map[x][y+1] == color:
        map[x][y+1] = newColor
        y += 1
    else:
        return
    return paintFill(map, x, y, color, newColor)