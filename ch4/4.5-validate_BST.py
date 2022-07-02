def validateBST(root):
    if root is None:
        return
    if root.left <= root:
        validateBST(root.left)
    else:
        return False
    if root.right >= root:
        validateBST(root.right)
    else:
        return False
    return True