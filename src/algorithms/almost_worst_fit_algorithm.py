from bin import Bin
from item import Item
from .worst_fit_algorithm import WorstFitAlgorithm

class AlmostWorstFitAlgorithm(WorstFitAlgorithm):
    NAME = 'Almost Worst Fit'

    # Returns the second suitable bin if possible and the first otherwise
    # TODO: Check if it is in agreement with the algorithm
    def findBin(self, bins):
        emptiestBins = self.findEmptiestBins(bins)
        index = 1 if (len(emptiestBins == 1)) else 0

        return emptiestBins[index]
