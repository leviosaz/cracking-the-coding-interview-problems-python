class SetOfStacks:
    def __init__(self, stack_max):
        self.stacks = [[]]
        self.stack_max = stack_max
    
    def push(self, plate):
        if len(self.stacks[-1]) < self.stack_max:
            self.stacks[-1].append(plate)    
            return
        self.stacks.append([plate])
        
    def pop(self):
        return self.stacks[-1].pop()
    
    def popAt(self, stack_number):
        self.stacks[stack_number].pop()

stack = SetOfStacks(3)
stack.push("plate")
stack.push("plate")
stack.push("plate")
stack.push("plate2")
stack.push("plate2")
stack.push("plate2")
stack.push("plate3")
stack.push("plate3")
stack.push("plate3")
    
print(stack.stacks)

stack.pop()
stack.popAt(1)

print(stack.stacks)

stack.push("plate3")
stack.push("plate4")

print(stack.stacks)