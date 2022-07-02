class TowersOfHanoi:
    def __init__(self):
        self.towers = {
                    "towerA": [14, 8, 6, 4, 2, 1],
                    "towerB": [30, 29, 14, 10],
                    "towerC": [14, 13, 12, 11, 10]
                    }      
        
    def __str__(self):
        return str(self.towers)
    
    def moveDisk(self, tower):
        disk = self.towers[tower].pop()
        
        for x in self.towers:
            if x == tower:
                continue
            
            if self.towers[x][-1] >= disk:
                return self.towers[x].append(disk)

tower = TowersOfHanoi()
print(tower)
tower.moveDisk("towerC")
print(tower)