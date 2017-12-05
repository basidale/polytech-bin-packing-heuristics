from bin import Bin
from item import Item

class BestFitAlgorithm:
    NAME = 'Best Fit'

    def findBin(self, bins, item, capacity):
        maxLoading = None
        mostFilledBins = list()
        
        for b in bins:
            if maxLoading is None or b.loading() > maxLoading:
                if item.isFittingInto(b):
                    maxLoading = b.loading()
                    del mostFilledBins[:]
                    mostFilledBins.append(b)
                    
            elif b.loading() == maxLoading:
                mostFilledBins.append(b)

        if len(mostFilledBins) > 0:
            return mostFilledBins[0]
        else:
            b = Bin(capacity)
            bins.append(b)
            return b

    def step(self, itemList, capacity, bins):
        item = itemList.pop(0)
        b = self.findBin(bins, item, capacity)
        b.addItem(item)

