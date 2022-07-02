class MultiStack:
    def __init__(self, number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.array = []
        for x in range(number_of_stacks):
            self.array.append([0])
    
    def pop(stack_number):
        self.array[stack_number].pop()
    
    def push(stack_number, element):
        self.array[stack_number].append(element)
    
    def push(stack_number):
        return self.array[stack_number][0]
    
    def isEmpty(stack_number):
        if len(self.array[stack_number]) == 0:
            return True 
        return False

