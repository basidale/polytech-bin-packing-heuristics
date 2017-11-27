from bin import Bin
from item import Item

class Simulation:
    
    def __init__(self, capacity, itemList, algorithm):
        self.capacity = capacity
        self.itemList = itemList
        self.algorithm = algorithm
        self.bins = [ Bin(capacity) ]
    
    def run(self):
        print('Algorithme : ' + self.algorithm.NAME)
        print('Capacité : ' + str(self.capacity))
        print('Items : ' + str(self.itemList))
        print('')

        self.printState()
        while len(self.itemList) > 0:
            self.algorithm.step(self.itemList, self.capacity, self.bins)
            self.printState()
    
    def printState(self):
        print('Items restants : ' + str(len(self.itemList)))
        
        for index, b in enumerate(self.bins):
            print('(' + str(index) + ') ' + str(b))

