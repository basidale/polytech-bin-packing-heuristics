from bin import Bin
from item import Item
from algorithms.AVLTree import AVLTree

class Simulation:
    def __init__(self, capacity, itemList, algorithm):
        self.capacity = capacity
        self.itemList = itemList
        self.algorithm = algorithm
        self.currentItem = None
        
    def run(self):
        print('Heuristique ' + self.algorithm.NAME)

        while not self.isCompleted():
            self.step()
            
    def step(self):
        # Pops next item in the list
        self.currentItem = self.itemList.pop(0)
        
        b = self.algorithm.findBin(self.currentItem, self.capacity)

    def isCompleted(self):
        return len(self.itemList) == 0
            
    def printState(self):
        print('Items restants : ' + str(len(self.itemList)))
        
        for index, b in enumerate(sorted(self.algorithm.getBins())):
            print('Bin n°' + str(index) + ' : ' + str(b))

            
