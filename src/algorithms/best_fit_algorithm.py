from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy
from .AVLTree import AVLTree

class BestFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Best Fit'

    def __init__(self):
        self.bst = AVLTree(key=lambda x : x.loading())

    @staticmethod
    def getName():
        return BestFitAlgorithm.NAME
    
    def findBin(self, item, capacity):
        current = self.bst.root
        best = None
        
        while current is not None:
            _bin = current.key
            
            if item.fitsInto(_bin):
                best = _bin
                if _bin.residual() == item.size:
                    current = None
                else:
                    current = current.right
            else:
                current = current.left

        _bin = None
        if best is None:
            _bin = Bin(capacity)
            _bin.addItem(item)
        else:
            self.bst.remove(best)
            _bin = best
            _bin.addItem(item)

        self.bst.insert(_bin)

        return _bin

            
    def getBins(self):
        return self.bst.values()
