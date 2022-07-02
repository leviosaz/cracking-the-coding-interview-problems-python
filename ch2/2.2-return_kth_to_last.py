from linked_list import LinkedList

def returnKthToLast(ll, k):
    nodes = []
    
    current = ll.head
    while current:
        nodes.append(current)
        current = current.next
    
    return nodes[-k]

linked_list = LinkedList()
linked_list.insert("3")
linked_list.insert("4")
linked_list.insert("5")
linked_list.insert("6")
linked_list.insert("7")
linked_list.insert("7")
print(linked_list)

print(returnKthToLast(linked_list, 3))