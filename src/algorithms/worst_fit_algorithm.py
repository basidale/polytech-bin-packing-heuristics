from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy
from .AVLTree import AVLTree

class WorstFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Worst Fit'

    def __init__(self):
        self.bst = AVLTree(key=lambda x : x.loading())
        
    @staticmethod
    def getName():
        return WorstFitAlgorithm.NAME
    
    def findBin(self, item, capacity):
        current = self.bst.root

        _bin = self.findWorst(item)
        if _bin is None:
            _bin = Bin(capacity)
        else:
            self.bst.remove(_bin)            

        _bin.addItem(item)
        self.bst.insert(_bin)

        return _bin
        
    def findWorst(self, item):
        current = self.bst.root
        worst = None
        
        while current is not None:
            _bin = current.key
            
            if item.fitsInto(_bin):
                worst = _bin
            current = current.left
        
        return worst

    def getBins(self):
        return self.bst.values()
