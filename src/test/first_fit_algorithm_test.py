import unittest
from bin import Bin
from item import Item
from algorithms import FirstFitAlgorithm

class FirstFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.firstFit = FirstFitAlgorithm()
        self.bins=list()
        self.bins.append(Bin(FirstFitAlgorithmTest.capacity))
        
    def test_findBin(self):
        capacity = FirstFitAlgorithmTest.capacity
        sizeItems=[ 50, 90, 10, 20, 40, 70, 15, 60, 15, 22 ]

        for size in sizeItems:
            item = Item(size)
            binQuantity = len(self.bins)

            expectedBin = self.expectedBin(item)
            binOpened = (expectedBin is None)
            expectedQuantity = binQuantity + (1 if binOpened else 0)
            expectedLoading = size + (0 if binOpened else expectedBin.loading())
            
            b = self.firstFit.findBin(item, capacity, self.bins)
            b.addItem(item)

            if not binOpened:
                self.assertEqual(expectedBin, b)
            self.assertEqual(expectedQuantity, len(self.bins))
            self.assertEqual(expectedLoading, b.loading())
            
    def expectedBin(self, item):
        fitting = [ e for e in self.bins if item.isFittingInto(e) ]

        if (len(fitting) == 0):
            return None

        fitting.sort()
        
        return fitting[0]
