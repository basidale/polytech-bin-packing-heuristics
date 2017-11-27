from bin import Bin
from item import Item

# Algorithme glouton
class NextFitAlgorithm:
    NAME = 'Next Fit'

    def __init__(self):
        self.currentBinIndex = 0
            
    def step(self, itemList, capacity, bins):
        item = itemList.pop(0)
            
        if (not item.isFittingInto(bins[self.currentBinIndex])):
            self.currentBinIndex += 1
            bins.append(Bin(capacity))
        
        bins[self.currentBinIndex].addItem(item)
    
            
