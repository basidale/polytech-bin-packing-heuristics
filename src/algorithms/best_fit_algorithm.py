from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class BestFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Best Fit'

    @staticmethod
    def getName():
        return NAME
    
    def findBin(self, item, capacity, bins):
        fitting = [ e for e in bins if item.isFittingInto(e) ]
        if (len(fitting) == 0):
            b = Bin(capacity)
            bins.append(b)
            return b
        
        fitting = sorted(fitting, key=lambda x: x.loading())
        bests = [ e for e in fitting if e.loading() == fitting[0].loading() ]
        bests.sort()
        
        return bests[0]

