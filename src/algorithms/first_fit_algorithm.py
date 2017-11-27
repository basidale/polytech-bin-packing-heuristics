from bin import Bin
from item import Item

class FirstFitAlgorithm:
    NAME = 'First Fit'

    def step(self, itemList, capacity, bins):
        item = itemList.pop(0)
        foundBin = False
        
        for b in bins:
            if item.isFittingInto(b):
                b.addItem(item)
                foundBin = True

        if not foundBin:
            b = Bin(capacity)
            b.addItem(item)
            bins.append(b)
