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
        bin_ = self.bins.pop() if len(self.bins) > 0 else None

        if bin_ is None or not item.fitsInto(bin_):
            bin_ = Bin(capacity)
        
        bin_.addItem(item)
        self.bins.append(bin_)
        
        return bin_

    def getBins(self):
        return self.bins
