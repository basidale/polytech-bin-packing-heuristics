from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

# Algorithme glouton
class NextFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Next Fit'

    def __init__(self):
        self.currentBinIndex = 0

    @staticmethod
    def getName():
        return NAME

    def findBin(self, item, capacity, bins):
        # If the item does not fits into the current bin,
        # add one bin to the list and increment current bin index
        if (not item.isFittingInto(bins[self.currentBinIndex])):
            bins.append(Bin(capacity))
            self.currentBinIndex += 1

        # Add the item to the current bin
        return bins[self.currentBinIndex]
