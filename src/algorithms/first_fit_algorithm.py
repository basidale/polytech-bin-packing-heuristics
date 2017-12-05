from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class FirstFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'First Fit'

    @staticmethod
    def getName():
        return NAME
    
    def findBin(self, item, capacity, bins):
        foundBin = False
        
        # Find the first suitable bin
        for b in bins:
            if item.isFittingInto(b):
                return b
        
        # If no bins are suitable add one bin to the list
        b = Bin(capacity)
        bins.append(b)

        return b

    
