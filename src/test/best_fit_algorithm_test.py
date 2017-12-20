import unittest
from bin import Bin
from item import Item
from algorithms import BestFitAlgorithm

class BestFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.bestFit = BestFitAlgorithm()
        self.bins=list()
        self.bins.append(Bin(BestFitAlgorithmTest.capacity))
        
    def test_findBin(self):
        capacity = BestFitAlgorithmTest.capacity
        sizeItems=[ 50, 90, 10, 20, 40, 70, 15, 60, 15, 22 ]

        for size in sizeItems:
            item = Item(size)
            binQuantity = len(self.bins)

            expectedBin = self.expectedBin(item)
            binOpened = (expectedBin is None)
            expectedQuantity = binQuantity + (1 if binOpened else 0)
            expectedLoading = size + (0 if binOpened else expectedBin.loading())
            
            b = self.bestFit.findBin(item, capacity, self.bins)
            b.addItem(item)

            if not binOpened:
                self.assertEqual(expectedBin, b)
            
            self.assertEqual(expectedQuantity, len(self.bins))
            self.assertEqual(expectedLoading, b.loading())
            
    def expectedBin(self, item):
        fitting = [ e for e in self.bins if item.isFittingInto(e) ]
        if (len(fitting) == 0):
            return None
        
        fitting = sorted(fitting, key=lambda x: x.loading(), reverse=True)
        bests = [ e for e in fitting if e.loading() == fitting[0].loading() ]
        bests.sort()
        
        return bests[0]
