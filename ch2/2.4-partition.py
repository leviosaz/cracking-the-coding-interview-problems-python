from linked_list import LinkedList

def partition(ll, pivot):
    less = []
    more = []
    
    current = ll.head
    while current:
        if current.value < pivot:
            less.append(current.value)
        else:
            more.append(current.value)
        
        current = current.next    

    ordered = less + more
    
    new_ll = LinkedList()
    for x in ordered:
        new_ll.insert(x)

    return new_ll

linked_list = LinkedList()
linked_list.insert(7)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(4)
linked_list.insert(3)
print(partition(linked_list, 5))