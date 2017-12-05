from bin import Bin
from item import Item

class FirstFitAlgorithm:
    NAME = 'First Fit'

    def step(self, itemList, capacity, bins):
        # Pops next item in the list
        item = itemList.pop(0)
        foundBin = False
        
        # Find the first suitable bin
        for b in bins:
            if item.isFittingInto(b):
                b.addItem(item)
                foundBin = True
        
        # If no bins are suitable add one bin to the list
        if not foundBin:
            b = Bin(capacity)
            b.addItem(item)
            bins.append(b)
