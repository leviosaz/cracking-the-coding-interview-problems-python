from linked_list import LinkedList

def palindrome(ll):
    theWord = ""
    
    curr = ll.head
    while curr:
        theWord += curr.value
        curr = curr.next
    
    pointerA = 0
    pointerB = len(theWord)-1
    
    while pointerA < pointerB:
        if theWord[pointerA] != theWord[pointerB]:
            return False
        pointerA += 1
        pointerB -= 1
    
    return True

word = LinkedList()
word.insert("k")
word.insert("a")
word.insert("y")
word.insert("a")
word.insert("k")
print(palindrome(word))

word2 = LinkedList()
word2.insert("c")
word2.insert("a")
word2.insert("t")
print(palindrome(word2))