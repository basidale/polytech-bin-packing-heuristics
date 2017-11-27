from bin import Bin
from item import Item

class WorstFitAlgorithm:
    NAME = 'Worst Fit'

    def findEmptiestBins(self, bins):
        minLoading = None
        emptiestBins = list()
        
        for b in bins:
            if minLoading is None or b.loading() < minLoading:
                minLoading = b.loading()
                del emptiestBins[:]
                emptiestBins.append(b)
            
            elif b.loading() == minLoading:
                emptiestBins.append(b)
        
        return emptiestBins

    def findBin(self, bins):
        return self.findEmptiestBins(bins)[0]

    def step(self, itemList, capacity, bins):
        item = itemList.pop(0)
        b = self.findBin(bins)
        
        if not item.isFittingInto(b):
            b = Bin(capacity)
            bins.append(b)

        b.addItem(item)

