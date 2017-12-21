from bin import Bin
from item import Item
from .worst_fit_algorithm import WorstFitAlgorithm
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class AlmostWorstFitAlgorithm(WorstFitAlgorithm):
    NAME = 'Almost Worst Fit'

    def findBin(self, item, capacity, bins):
        fitting = [ e for e in bins if item.isFittingInto(e) ]
        fitting.sort()
        fitting.sort(key=lambda x: x.loading())
        
        if (len(fitting) == 0):
            b = Bin(capacity)
            bins.append(b)
            return b
        else:
            worsts = [ e for e in fitting if e.loading() == fitting[0].loading() ]
            remaining = [e for e in fitting if e.loading() > worsts[0].loading() ]
            
            if len(remaining) == 0:
                return worsts[0]
            else:
                return remaining[0]


