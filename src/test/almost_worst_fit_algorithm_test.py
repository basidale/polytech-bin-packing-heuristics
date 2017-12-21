import unittest
from bin import Bin
from item import Item
from algorithms import AlmostWorstFitAlgorithm

class AlmostWorstFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.almostWorstFit = AlmostWorstFitAlgorithm()
        self.bins=list()
        self.bins.append(Bin(AlmostWorstFitAlgorithmTest.capacity))
        self.item80 = Item(80)
        self.item40 = Item(40)
        self.item10 = Item(10)

        
    def test_findBin_general_case(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity
        
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

        b = self.almostWorstFit.findBin(self.item10, capacity, self.bins)
        b.addItem(self.item10)

        self.assertEqual(80, b80.loading())
        self.assertEqual(50, b40.loading())
        self.assertEqual(10, b10.loading())
        self.assertEqual(3, len(self.bins))
        
    def test_findBin_one_only_bin(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity
        
        self.bins[0].addItem(self.item40)
        
        b = self.almostWorstFit.findBin(self.item10, capacity, self.bins)
        b.addItem(self.item10)
        
        self.assertEqual(50, self.bins[0].loading())
        self.assertEqual(1, len(self.bins))
        
    def test_findBin_one_fitting_bin(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity

        # General case
        b80 = Bin(capacity)
        b80.addItem(self.item80)
        
        b40 = Bin(capacity)
        b40.addItem(self.item40)
        
        self.bins[0] = b80
        self.bins.append(b40)
        
        b = self.almostWorstFit.findBin(self.item80, capacity, self.bins)
        b.addItem(self.item80)
        
        self.assertEqual(3, len(self.bins))        
        self.assertEqual(80, self.bins[2].loading())        

    def test_no_fitting_bin(self):
        capacity = AlmostWorstFitAlgorithmTest.capacity
                
        b80 = Bin(capacity)
        b80.addItem(self.item80)

        self.bins[0] = b80

        b = self.almostWorstFit.findBin(self.item40, capacity, self.bins)
        b.addItem(self.item40)

        self.assertEqual(80, b80.loading())
        self.assertEqual(2, len(self.bins))
        self.assertEqual(40, self.bins[1].loading())
