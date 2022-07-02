def checkBalanced(root):
        
    def maxDepth(root):
        if root is None:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))

    def minDepth(root):
        if root is None:
            return 0
        return 1 + max(minDepth(root.left), minDepth(root.right))
    
    max = maxDepth(root)
    min = minDepth(root)
    
    return max - min <= 1