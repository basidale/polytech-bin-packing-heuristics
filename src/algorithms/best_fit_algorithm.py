from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class BestFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Best Fit'

    @staticmethod
    def getName():
        return NAME
    
    def findBin(self, item, capacity, bins):
        maxLoading = None
        mostFilledBins = list()

        # Finds the bin with the maximal residual capacity
        for b in bins:
            if maxLoading is None or b.loading() > maxLoading:
                if item.isFittingInto(b):
                    maxLoading = b.loading()
                    del mostFilledBins[:]
                    mostFilledBins.append(b)
                    
            elif b.loading() == maxLoading:
                mostFilledBins.append(b)

        # If there are more than one suitable bin, we choose the first
        if len(mostFilledBins) > 0:
            return mostFilledBins[0]
        # If no bins is suitable, we open a new bin
        else:
            b = Bin(capacity)
            bins.append(b)
            return b

    def step(self, itemList, capacity, bins):
        # Pops next item in the list
        item = itemList.pop(0)
        
        # Finds the most suitable bin
        b = self.findBin(bins, item, capacity)
        
        # Adds the item to the list
        b.addItem(item)

