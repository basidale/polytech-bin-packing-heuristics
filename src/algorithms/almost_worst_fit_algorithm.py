from bin import Bin
from item import Item
from .worst_fit_algorithm import WorstFitAlgorithm
from .bp_algorithm_strategy import IBinPackingAlgorithmStrategy

class AlmostWorstFitAlgorithm(WorstFitAlgorithm):
    NAME = 'Almost Worst Fit'

    def findBin(self, item, capacity, bins):
        sortedBins = sorted(bins, key=lambda x: x.loading())
        sortedBins.sort()
        
        emptiest = sortedBins[0]
        secondEmptiest = None

        if (len(sortedBins) > 1):
            sortedBins = [e for e in sortedBins if e.loading() != sortedBins[0].loading()]
            secondEmptiest = sortedBins[0]

        b = None
        if secondEmptiest is not None and item.isFittingInto(secondEmptiest):
            b = secondEmptiest
        elif item.isFittingInto(emptiest):
            b = emptiest
        else:
            b = Bin(capacity)
            bins.append(b)
        
        return b
