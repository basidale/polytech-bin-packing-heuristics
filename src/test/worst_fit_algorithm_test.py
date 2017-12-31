import unittest
from bin import Bin
from item import Item
from algorithms import WorstFitAlgorithm
from algorithms.AVLTree import AVLTree

class WorstFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.worstFit = WorstFitAlgorithm()
        
    def test_findBin(self):
        capacity = WorstFitAlgorithmTest.capacity

        # General case
        b80 = WorstFitAlgorithmTest.binOfLoading(80)
        b40 = WorstFitAlgorithmTest.binOfLoading(40)
        b10 = WorstFitAlgorithmTest.binOfLoading(10)

        bins = list()
        bins.append(b80)
        bins.append(b40)
        bins.append(b10)
        
        bst = AVLTree(key=lambda x : x.loading())
        for _bin in bins:
            bst.insert(_bin)

        self.worstFit.bst = bst
        b = self.worstFit.findBin(Item(10), capacity)

        self.assertEqual(b, b10)
        self.assertEqual(80, b80.loading())
        self.assertEqual(40, b40.loading())
        self.assertEqual(20, b10.loading())
        self.assertEqual(3, len(bins))
        
        b = self.worstFit.findBin(Item(40), capacity)

    def test_two_candidates(self):
        capacity = WorstFitAlgorithmTest.capacity
        
        # General case
        b40 = WorstFitAlgorithmTest.binOfLoading(40)
        b40b = WorstFitAlgorithmTest.binOfLoading(40)
        
        bins = list()
        bins.append(b40)
        bins.append(b40b)
        
        bst = AVLTree(key=lambda x : x.loading())
        for _bin in bins:
            bst.insert(_bin)

        self.worstFit.bst = bst
        b = self.worstFit.findBin(Item(10), capacity)
        
        self.assertEqual(50, b40.loading())
        self.assertEqual(40, b40b.loading())

        self.worstFit.bst = bst
        b = self.worstFit.findBin(Item(60), capacity)
        
        self.assertEqual(50, b40.loading())
        self.assertEqual(100, b40b.loading())


    def test_findBin_updateBST(self):
        capacity = WorstFitAlgorithmTest.capacity

        b80 = WorstFitAlgorithmTest.binOfLoading(80)
        b40 = WorstFitAlgorithmTest.binOfLoading(40)
        b10 = WorstFitAlgorithmTest.binOfLoading(10)

        bins = list()
        bins.append(b80)
        bins.append(b40)
        bins.append(b10)
        
        bst = AVLTree(key=lambda x : x.loading())
        for _bin in bins:
            bst.insert(_bin)
 
        self.worstFit.bst = bst
        b = self.worstFit.findBin(Item(40), capacity)

        self.assertEqual(b, b10)
        self.assertEqual(80, b80.loading())
        self.assertEqual(40, b40.loading())
        self.assertEqual(50, b10.loading())
        self.assertEqual(3, len(bins))
        
        self.worstFit.bst = bst
        b = self.worstFit.findBin(Item(10), capacity)

        self.assertEqual(b, b40)
        self.assertEqual(80, b80.loading())
        self.assertEqual(50, b40.loading())
        self.assertEqual(50, b10.loading())
        self.assertEqual(3, len(bins))

    def test_no_fitting_bin(self):
        capacity = WorstFitAlgorithmTest.capacity

        b80 = WorstFitAlgorithmTest.binOfLoading(80)
        bins = list()
        bins.append(b80)
        
        bst = AVLTree(key=lambda x : x.loading())
        for _bin in bins:
            bst.insert(_bin)

        self.worstFit.bst = bst
        b = self.worstFit.findBin(Item(40), capacity)

        bins = sorted(bst.values())
        self.assertEqual(80, b80.loading())
        self.assertEqual(2, len(bins))
        self.assertEqual(40, bins[1].loading())
    
    @staticmethod
    def binOfLoading(loading):
        bin_ = Bin(WorstFitAlgorithmTest.capacity)
        bin_.addItem(Item(loading))
        return bin_
