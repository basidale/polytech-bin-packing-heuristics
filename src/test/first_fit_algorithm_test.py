import unittest
from bin import Bin
from item import Item
from algorithms import FirstFitAlgorithm

class FirstFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.firstFit = FirstFitAlgorithm()
        
    def test_findBin(self):
        capacity = FirstFitAlgorithmTest.capacity
        sizeItems=[ 50, 90, 10, 20, 40, 70, 15, 60, 15, 22, 11, 95, 52, 15, 32, 63 ]
        currentIndex = 0
        binQuantity = 0

        for size in sizeItems:
            item = Item(size)

            bins = self.firstFit.getBins()
            
            # Filter bins where item fits in
            fitting = [ e for e in bins if item.fitsInto(e) ]

            if len(fitting) > 0:
                expectedBin = fitting[0]

            b = self.firstFit.findBin(item, capacity)
            
            if len(fitting) > 0:
                self.assertEqual(expectedBin, b);
            else:
                bins = sorted(self.firstFit.getBins())
                self.assertEqual(binQuantity + 1, len(bins))

            binQuantity = len(self.firstFit.getBins())
