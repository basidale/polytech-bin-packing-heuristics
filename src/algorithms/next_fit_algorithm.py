from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

# Algorithme glouton
class NextFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Next Fit'

    def __init__(self):
        self.currentBinIndex = 0
        self.bins = [ ]
        
    @staticmethod
    def getName():
        return NextFitAlgorithm.NAME

    def findBin(self, item, capacity):
        if len(self.bins) == 0:
            self.bins.append(Bin(capacity))
        
        # If the item does not fits into the current bin,
        # add one bin to the list and increment current bin index
        if (not item.fitsInto(self.bins[self.currentBinIndex])):
            self.bins.append(Bin(capacity))
            self.currentBinIndex += 1
        
        # Add the item to the current bin
        bin_ = self.bins[self.currentBinIndex]
        bin_.addItem(item)
        
        return bin_

    def getBins(self):
        return self.bins
