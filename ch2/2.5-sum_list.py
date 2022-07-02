# Idea (after doing this): We can avoid creating a new linked list by traversing through both linked lists at the same time
# And then we add the values together and store in one of them
# Then we hold the carrying term to add to the next value of the linked list
from linked_list import LinkedList

def sumList(l1,l2):
    def get_num(head):
        num = 0
        while head:
            num = num * 10 + head.value
            head = head.next
        return num
    
    num1 = get_num(l1.head)
    num2 = get_num(l2.head)
    
    final = str(num1 + num2)
    finalLL = LinkedList()
    for x in final:
        finalLL.insert(int(x))
    
    return finalLL
    
    
one = LinkedList()
one.insert(2)
one.insert(3)
one.insert(4)

two = LinkedList()
two.insert(9)
two.insert(9)
two.insert(2)

print(sumList(one, two))
