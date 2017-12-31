import unittest
from bin import Bin
from item import Item
from algorithms import AlmostWorstFitAlgorithm
from algorithms.AVLTree import AVLTree

class AlmostWorstFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.almostWorstFit = AlmostWorstFitAlgorithm()
        self.bins=list()

    def test_findBin_general_case(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity
        
        # General case
        b80 = AlmostWorstFitAlgorithmTest.binOfLoading(80)
        b40 = AlmostWorstFitAlgorithmTest.binOfLoading(40)
        b10 = AlmostWorstFitAlgorithmTest.binOfLoading(10)
        
        self.bins.append(b80)
        self.bins.append(b40)
        self.bins.append(b10)

        bst = AVLTree()
        for _bin in self.bins:
            bst.insert(_bin)
        
        self.almostWorstFit.bst = bst
        b = self.almostWorstFit.findBin(Item(10), capacity)

        self.assertEqual(80, b80.loading())
        self.assertEqual(50, b40.loading())
        self.assertEqual(10, b10.loading())
        self.assertEqual(3, len(self.bins))
        
    def test_findBin_one_only_bin(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity

        b40 = AlmostWorstFitAlgorithmTest.binOfLoading(40)

        self.bins.append(b40)

        bst = AVLTree()
        for _bin in self.bins:
            bst.insert(_bin)

        self.almostWorstFit.bst = bst
        b = self.almostWorstFit.findBin(Item(10), capacity)
        
        self.assertEqual(50, self.bins[0].loading())
        self.assertEqual(1, len(self.bins))
        

    # TODO : Redo
    def test_findBin_one_fitting_bin(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity

        # General case
        b80 = AlmostWorstFitAlgorithmTest.binOfLoading(80)
        b40 = AlmostWorstFitAlgorithmTest.binOfLoading(40)
        
        self.bins.append(b80)
        self.bins.append(b40)

        bst = AVLTree()
        for _bin in self.bins:
            bst.insert(_bin)

        self.almostWorstFit.bst = bst
        b = self.almostWorstFit.findBin(Item(80), capacity)
        
        bins = sorted(self.almostWorstFit.getBins())
        self.assertEqual(3, len(bins))
        self.assertEqual(80, bins[2].loading())        

    def test_no_fitting_bin(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity
                
        b80 = AlmostWorstFitAlgorithmTest.binOfLoading(80)

        self.bins.append(b80)

        bst = AVLTree()
        for _bin in self.bins:
            bst.insert(_bin)
        
        self.almostWorstFit.bst = bst
        b = self.almostWorstFit.findBin(Item(40), capacity)

        bins = sorted(self.almostWorstFit.getBins())
        self.assertEqual(80, b80.loading())
        self.assertEqual(2, len(bins))
        self.assertEqual(40, bins[1].loading())

    def test_findbin2(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity
        sizeItems=[ 50, 90, 10, 20, 40, 70, 15, 60, 15, 22 ]
        currentIndex = 0
        binQuantity = len(self.bins)
        
        for size in sizeItems:
            item = Item(size)

            bins = self.almostWorstFit.getBins()
            expectedBin = self.findExpectedBin(bins, item)

            b = self.almostWorstFit.findBin(item, capacity)

            bins = self.almostWorstFit.getBins()
            if expectedBin is not None:
                self.assertEqual(expectedBin, b)
            else:
                self.assertEqual(binQuantity + 1, len(bins))
                self.assertEqual(size, b.loading());
            
            binQuantity = len(bins)
            
    def findExpectedBin(self, bins, item):
        fitting = [ e for e in bins if item.fitsInto(e) ]
        fitting.sort()
        fitting.sort(key=lambda x: x.loading())
        
        if (len(fitting) == 0):
            return None

        bin_ = None
        worsts = [ e for e in fitting if e.loading() == fitting[0].loading() ]
        remaining = [e for e in fitting if e.loading() > worsts[0].loading() ]
        
        if len(remaining) == 0:
            bin_ = worsts[0]
        else:
            bin_ = remaining[0]

        return bin_

    @staticmethod
    def binOfLoading(loading):
        bin_ = Bin(AlmostWorstFitAlgorithmTest.capacity)
        bin_.addItem(Item(loading))
        return bin_
