from bin import Bin
from item import Item
from .worst_fit_algorithm import WorstFitAlgorithm
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class AlmostWorstFitAlgorithm(WorstFitAlgorithm):
    NAME = 'Almost Worst Fit'

    def findBin(self, item, capacity, bins):
        fitting = [ e for e in bins if item.isFittingInto(e) ]
        if (len(fitting) == 0):
            b = Bin(capacity)
            bins.append(b)
            return b
        
        fitting = sorted(fitting, key=lambda x: x.loading(), reverse=True)
        worsts = [ e for e in fitting if e.loading() == fitting[0].loading() ]
        worsts.sort()

        if (len(worsts) == 1):
            return worsts[0]
        return worsts[1]
