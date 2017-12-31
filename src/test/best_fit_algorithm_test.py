import unittest
from bin import Bin
from item import Item
from algorithms import BestFitAlgorithm
from algorithms.AVLTree import AVLTree

class BestFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.bestFit = BestFitAlgorithm()
        self.bins=list()
        self.bins.append(Bin(BestFitAlgorithmTest.capacity))
        self.item80 = Item(80)
        self.item40 = Item(40)
        self.item10 = Item(10)
        
    def test_findBin_general_case(self):
        capacity = BestFitAlgorithmTest.capacity
        
        # General case
        b80 = Bin(capacity)
        b80.addItem(self.item80)
        
        b40 = Bin(capacity)
        b40.addItem(self.item40)

        b10 = Bin(capacity)
        b10.addItem(self.item10)

        self.bins[0] = b80
        self.bins.append(b40)
        self.bins.append(b10)
        
        bst = AVLTree(key=lambda x : x.loading())
        for _bin in self.bins:
            bst.insert(_bin)

        self.bestFit.bst = bst
        b = self.bestFit.findBin(self.item10, capacity)

        self.assertEqual(90, b80.loading())
        self.assertEqual(40, b40.loading())
        self.assertEqual(10, b10.loading())
        self.assertEqual(3, len(self.bins))

    def test_two_candidates(self):
        capacity = BestFitAlgorithmTest.capacity
        
        # General case
        b40 = Bin(capacity)
        b40.addItem(self.item40)
        
        b40b = Bin(capacity)
        b40b.addItem(self.item40)
        
        self.bins[0] = b40
        self.bins.append(b40b)
        
        bst = AVLTree(key=lambda x : x.loading())
        for _bin in self.bins:
            bst.insert(_bin)

        self.bestFit.bst = bst
        b = self.bestFit.findBin(self.item10, capacity)
        
        self.assertEqual(50, b40.loading())
        self.assertEqual(40, b40b.loading())

        self.bestFit.bst = bst
        b = self.bestFit.findBin(Item(60), capacity)
        
        self.assertEqual(50, b40.loading())
        self.assertEqual(100, b40b.loading())
        
    def test_no_fitting_bin(self):
        capacity = BestFitAlgorithmTest.capacity
                
        b80 = Bin(capacity)
        b80.addItem(self.item80)

        self.bins[0] = b80

        bst = AVLTree(key=lambda x : x.loading())
        for _bin in self.bins:
            bst.insert(_bin)

        self.bestFit.bst = bst
        b = self.bestFit.findBin(self.item40, capacity)

        bins = sorted(bst.values())
        self.assertEqual(2, len(bins))
        self.assertEqual(80, bins[0].loading())
        self.assertEqual(40, bins[1].loading())
        
    def test_findbin2(self):
        capacity = BestFitAlgorithmTest.capacity
        sizeItems=[ 50, 90, 10, 20, 40, 70, 15, 60, 15, 22, 91, 34, 50, 13 ]
        currentIndex = 0
        binQuantity = 0
        
        for size in sizeItems:
            item = Item(size)
            bins = self.bestFit.getBins()
            expectedBin = self.findExpectedBin(bins, item)

            b = self.bestFit.findBin(item, capacity)

            bins = sorted(self.bestFit.getBins())
            if expectedBin is not None:
                self.assertEqual(expectedBin, b)
            else:
                self.assertEqual(binQuantity + 1, len(bins))
                self.assertEqual(size, b.loading());
            
            binQuantity = len(bins)
            
    def findExpectedBin(self, bins, item):
        fitting = [ e for e in bins if item.fitsInto(e) ]
        
        if (len(fitting) == 0):
            return None
        
        fitting.sort(key=lambda x: x.loading(), reverse=True)
        bests = [ e for e in fitting if e.loading() == fitting[0].loading() ]
        bests.sort()
        
        return bests[0]
