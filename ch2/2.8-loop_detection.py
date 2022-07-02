from linked_list import LinkedList

def loopDetection(ll):
    slow = fast = ll.head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next 
        if fast == slow:
            break
    
    if fast != None or fast.next != None:
        return False
    return True
    
    