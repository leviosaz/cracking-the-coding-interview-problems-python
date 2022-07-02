class MyQueue:
    def __init__(self, iterable):
        self.queue = [] # Stores things backwards
        
        for x in range(len(iterable)-1, -1, -1):
            self.queue.append(iterable[x])
            
    def add(self, element):
        self.queue = [element] + self.queue
        return self.queue
    
    def remove(self):
        self.queue = self.queue[1:]
        return self.queue
    
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)
         
myq = MyQueue("hello")
myq.add("a")
print(myq)
myq.remove()
print(myq)
print(myq.peek())
print(myq.isEmpty())