class AnimalShelter:
    def __init__(self, iterable):
        self.shelter = iterable
        
    def __str__(self):
        return str(self.shelter)
        
    def enqueue(self, name, animal):
        self.shelter.append([name, animal])
        return [name, animal]
    
    def dequeueAny(self):
        animal = self.shelter[0]
        self.shelter = self.shelter[1:]
        return animal

    def dequeueDog(self):
        for x in range(len(self.shelter)):
            if self.shelter[x][1] == 'dog':
                if x == len(self.shelter):
                    return self.shelter.pop()
                theDog = self.shelter[x]
                self.shelter = self.shelter[0:x] + self.shelter[x+1:]
                return theDog
        return "No dogs in the shelter."    
    
    def dequeueCat(self):
        for x in range(len(self.shelter)):
            if self.shelter[x][1] == 'cat':
                if x == len(self.shelter):
                    return self.shelter.pop()
                theCat = self.shelter[x]
                self.shelter = self.shelter[0:x] + self.shelter[x+1:]
                return theCat
        return "No cats in the shelter."

shelter = AnimalShelter([["bob", "dog"], ["carl", "cat"]])
shelter.enqueue('ackerman', 'dog')
print(shelter)
shelter.dequeueDog()
print(shelter)
    