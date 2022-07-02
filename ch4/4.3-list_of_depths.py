from ch2.linked_list import LinkedList
from collections import deque

def listOfDepths(root):
    counter = 1
    hashmap = {}
    queue = deque()
    queue.append(root)
    
    def bfs(root)
        if root is None:
            return
        queue.append(root.left, root.right)
        bfs(root.left)
        bfs(root.right)
        return 
    
    while queue:
        ll = LinkedList()
        for x in range(2**counter)
            item = queue.popleft()
            ll.insert(item)
        hashmap[counter] = ll
        counter += 1
    
    return hashmap
        
    
    