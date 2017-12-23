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
        sizeItems=[ 50, 90, 10, 20, 40, 70, 15, 60, 15, 22 ]
        currentIndex = 0
        binQuantity = len(self.bins)

        for size in sizeItems:
            item = Item(size)
            b = self.nextFit.findBin(item, capacity, self.bins)

            if (len(self.bins) > binQuantity):
                self.assertEqual(binQuantity + 1, len(self.bins))
            self.assertEqual(b, self.bins[-1])
            
            binQuantity = len(self.bins)
