from bin import Bin
from item import Item
from .worst_fit_algorithm import WorstFitAlgorithm
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class AlmostWorstFitAlgorithm(WorstFitAlgorithm):
    NAME = 'Almost Worst Fit'

    # Returns the second suitable bin if possible and the first otherwise
    # TODO: Check if it is in agreement with the algorithm
    def findBin(self, item, capacity, bins):
        emptiestBins = self.findEmptiestBins(bins)
        index = 1 if (len(emptiestBins) > 1) else 0
        b = emptiestBins[index]
        
        # If no bin is suitable, we add one bin to the list
        if not item.isFittingInto(b):
            b = Bin(capacity)
            bins.append(b)
        
        return b
