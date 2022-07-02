from linked_list import LinkedList

def deleteMidNode(c):
    c.next = c.next.next

linked_list = LinkedList()
linked_list.insert("3")
linked_list.insert("4")
linked_list.insert("5")
node = linked_list.insert("6")
linked_list.insert("7")
linked_list.insert("7")
print(linked_list)
deleteMidNode(node)
print(linked_list)