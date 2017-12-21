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
        currentIndex = 0
        binQuantity = len(self.bins)

        for size in sizeItems:
            item = Item(size)
            
            # Filter bins where item fits in
            fitting = [ e for e in self.bins if item.isFittingInto(e) ]
            
            if len(fitting) > 0:
                expectedBin = fitting[0]
            
            b = self.firstFit.findBin(item, capacity, self.bins)
            b.addItem(item)

            if len(fitting) > 0:
                self.assertEqual(expectedBin, b);
            else:
                self.assertEqual(binQuantity + 1, len(self.bins))
                self.assertEqual(self.bins[-1], b);

            binQuantity = len(self.bins)
