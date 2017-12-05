from bin import Bin
from item import Item
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class WorstFitAlgorithm(IBinPackingAlgorithmStrategy):
    NAME = 'Worst Fit'
    
    @staticmethod
    def getName():
        return NAME
    
    def findEmptiestBins(self, bins):
        minLoading = None
        emptiestBins = list()
        
        # Finds the bin with the minimal residual capacity
        for b in bins:
            if minLoading is None or b.loading() < minLoading:
                minLoading = b.loading()
                del emptiestBins[:]
                emptiestBins.append(b)
            
            elif b.loading() == minLoading:
                emptiestBins.append(b)
        
        return emptiestBins
    
    # Returns the first among all suitable bins
    def findBin(self, item, capacity, bins):
        b = self.findEmptiestBins(bins)[0]

        # If no bin is suitable, we add one bin to the list
        if not item.isFittingInto(b):
            b = Bin(capacity)
            bins.append(b)

        return b
