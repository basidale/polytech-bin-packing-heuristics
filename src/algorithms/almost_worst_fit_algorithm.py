from bin import Bin
from item import Item
from .worst_fit_algorithm import WorstFitAlgorithm

class AlmostWorstFitAlgorithm(WorstFitAlgorithm):
    NAME = 'Almost Worst Fit'

    def findBin(self, bins):
        emptiestBins = self.findEmptiestBins(bins)
        index = 1
        if len(emptiestBins) == 1:
            index = 0
        return emptiestBins[index]
