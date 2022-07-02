class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        return newNode
        
    def __str__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.value)
            node = node.next
            while node:
                result += ", " + str(node.value)
                node = node.next
        result += "]"
        return result 
    