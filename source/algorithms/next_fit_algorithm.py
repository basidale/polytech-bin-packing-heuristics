from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy
from collections import deque

# Algorithme glouton
class NextFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Next Fit'

    def __init__(self):
        self.bins = deque()
        
    @staticmethod
    def getName():
        return NextFitAlgorithm.NAME

    def findBin(self, item, capacity):
        if len(self.bins) == 0:
            self.bins.append(Bin(capacity))
            
        bin_ = self.bins.pop()
        self.bins.append(bin_)
            
        if not item.fitsInto(bin_):
            bin_ = Bin(capacity)
            self.bins.append(bin_)

        bin_.addItem(item)
                
        return bin_

    def getBins(self):
        return self.bins
