from bin import Bin
from item import Item

# Algorithme glouton
class NextFitAlgorithm:
    NAME = 'Next Fit'

    def __init__(self):
        self.currentBinIndex = 0

    def step(self, itemList, capacity, bins):
        # Pops next item in the list
        item = itemList.pop(0)

        # If the item does not fits into the current bin,
        # add one bin to the list and increment current bin index
        if (not item.isFittingInto(bins[self.currentBinIndex])):
            self.currentBinIndex += 1
            bins.append(Bin(capacity))

        # Add the item to the current bin
        bins[self.currentBinIndex].addItem(item)
    
            
