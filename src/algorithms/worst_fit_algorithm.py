from bin import Bin
from item import Item

class WorstFitAlgorithm:
    NAME = 'Worst Fit'

    def findEmptiestBins(self, bins):
        minLoading = None
        emptiestBins = list()

        # Finds the bin with the minimal residual capacity
        for b in bins:
            if minLoading is None or b.loading() < minLoading:
                minLoading = b.loading()
                del emptiestBins[:]
                emptiestBins.append(b)
            
            elif b.loading() == minLoading:
                emptiestBins.append(b)
        
        return emptiestBins

    # Returns the first among all suitable bins
    def findBin(self, bins):
        return self.findEmptiestBins(bins)[0]
    
    def step(self, itemList, capacity, bins):
        # Pops next item in the list
        item = itemList.pop(0)
        
        # Finds the most suitable bin
        b = self.findBin(bins)
        
        # If no bin is suitable, we add one bin to the list
        if not item.isFittingInto(b):
            b = Bin(capacity)
            bins.append(b)
        
        # Adds the item to the list
        b.addItem(item)

