def minimalTree(array, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    parent = Node(array[mid])
    parent.left = minimalTree(array, start, mid - 1)
    parent.right = minimalTree(array, mid + 1, end)
    return parent
    