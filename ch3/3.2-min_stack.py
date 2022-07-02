class MinStack:
    def __init__(self, elements):
        self.array = []
        self.minimum = float('inf')
        
        for x in elements:
            if x < self.minimum:
                self.minimum = x
            self.array.append(x)

    def pop(self):
        self.array.pop()
        self.minimum = min(self.array)
    
    def push(self, element):
        if element < self.minimum:
            self.minimum = element
        self.array.append(element)


stack = MinStack([1, 2, 3, 4, 5])
print(stack.minimum)
print(stack.push(0))
print(stack.minimum)
print(stack.pop())
print(stack.minimum)    