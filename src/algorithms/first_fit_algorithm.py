from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy
from .AVLTree import AVLTree

class FirstFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'First Fit'

    def __init__(self):
        self.bst = AVLTree()

    @staticmethod
    def getName():
        return NAME
    
    def findBin(self, item, capacity):
        current = self.bst.root
        bin_ = None

        while current is not None:
            if item.fitsInto(current.key):
                bin_ = current.key
            
            if current.left is not None and current.left.minLoading + item.size <= capacity:
                current = current.left
            elif bin_ is None and current.right is not None and current.right.minLoading + item.size <= capacity:
                current = current.right
            else:
                current = None
        
        if not bin_:
            bin_ = Bin(capacity)
        else:
            self.bst.remove(bin_)

        bin_.addItem(item)
        self.bst.insert(bin_)

        return bin_
    
    def getBins(self):
        return self.bst.values()
