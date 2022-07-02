from linked_list import LinkedList

def intersection(l1, l2):
    
    def get_items(ll):
        curr = ll.head
        li = []
        while curr:
            li.append(curr)
            curr.next
        return li
    
    li1 = get_items(l1)
    li2 = get_items(l2)
    
    if li1[-1] != li2[-1]:
        return False
    
    pointer = 0
    intersection = None
    
    while li1[len(li1)-1-pointer] == li1[len(li2)-1-pointer]:
        intersection = li1[len(li1)-1-pointer]
        pointer += 1
    
    return intersection