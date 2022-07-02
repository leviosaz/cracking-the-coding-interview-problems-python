from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def routeBetweenNodes(graph, start, end):
    if start == end:
        return True 
    
    visited = set()
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if adj not in visited:
                if adj == end:
                    return True 
                queue.append(adj)
        visited.add(node)
    return False