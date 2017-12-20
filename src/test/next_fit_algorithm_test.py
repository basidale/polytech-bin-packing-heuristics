import unittest
from bin import Bin
from item import Item
from algorithms import NextFitAlgorithm

class NextFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.nextFit = NextFitAlgorithm()
        self.bins=list()
        self.bins.append(Bin(NextFitAlgorithmTest.capacity))
    
    def test_findBin(self):
        capacity = NextFitAlgorithmTest.capacity
        sizeItems=[50, 90, 10, 20, 40, 70]

        for size in sizeItems:
            item = Item(size)
            current = self.bins[self.nextFit.currentBinIndex]
            initialLoading = current.loading()
            binQuantity = len(self.bins)
            
            b = self.nextFit.findBin(item, capacity, self.bins)
            b.addItem(item)

            binOpened = ((initialLoading + size) > capacity)
            expectedQuantity = binQuantity + (1 if binOpened else 0)
            expectedLoading = size + (0 if binOpened else initialLoading)

            self.assertEqual(expectedQuantity, len(self.bins))
            self.assertEqual(expectedLoading, b.loading())
        
        
        
