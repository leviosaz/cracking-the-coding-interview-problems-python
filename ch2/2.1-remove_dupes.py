from linked_list import LinkedList, Node

def removeDuplicates(ll):
    current = ll.head
    previous = None
    seen = set()
    
    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    return ll

linked_list = LinkedList()
linked_list.insert("3")
linked_list.insert("4")
linked_list.insert("5")
linked_list.insert("6")
linked_list.insert("7")
linked_list.insert("7")
print(linked_list)
removeDuplicates(linked_list)
print(linked_list)