from bin import Bin
from item import Item
from .worst_fit_algorithm import WorstFitAlgorithm
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy
from algorithms.AVLTree import AVLTree

class AlmostWorstFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Almost Worst Fit'

    def __init__(self):
        self.bst = AVLTree(key=lambda x : x.loading())
        self.bins = list()
        
    @staticmethod
    def getName():
        return NAME

    def findBin(self, item, capacity):
        bin_ = self.bst.select(1)

        if bin_ is not None and item.fitsInto(bin_):
            self.bst.remove(bin_)
        else:
            bin_ = self.bst.select(0)
            
            if bin_ is not None and item.fitsInto(bin_):
                self.bst.remove(bin_)
            else:
                bin_ = Bin(capacity)
                self.bins.append(bin_)
        
        bin_.addItem(item)
        self.bst.insert(bin_)
        
        return bin_
        
    def getBins(self):
        return self.bst.values()
