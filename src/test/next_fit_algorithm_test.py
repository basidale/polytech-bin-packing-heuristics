import unittest
from bin import Bin
from item import Item
from algorithms import NextFitAlgorithm

class NextFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.nextFit = NextFitAlgorithm()
    
    def test_findBin(self):
        capacity = NextFitAlgorithmTest.capacity
        sizeItems=[ 50, 90, 10, 20, 40, 70, 15, 60, 15, 22 ]
        currentIndex = 0
        binQuantity = 0

        for size in sizeItems:
            item = Item(size)
            b = self.nextFit.findBin(item, capacity)

            bins = self.nextFit.getBins()
            if (len(bins) > binQuantity):
                self.assertEqual(binQuantity + 1, len(bins))
            self.assertEqual(b, bins[-1])
            
            binQuantity = len(bins)
