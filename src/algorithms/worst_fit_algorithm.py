from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy
from .bin_bst import BinBST

class WorstFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Worst Fit'

    def __init__(self):
        self.bst = None
        
    @staticmethod
    def getName():
        return NAME
    
    def findBin(self, item, capacity, bins):
        if self.bst is None:
            self.bst = BinBST()
            for bin_ in bins:
                self.bst.insert(bin_)
        
        bin_ = self.bst.removeMin()
        
        if not item.isFittingInto(bin_):
            bin_ = Bin(capacity)
            bins.append(bin_)

        bin_.addItem(item)
        self.bst.insert(bin_)
        
        return bin_
