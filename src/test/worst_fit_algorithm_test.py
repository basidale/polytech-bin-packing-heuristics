import unittest
from bin import Bin
from item import Item
from algorithms import WorstFitAlgorithm

class WorstFitAlgorithmTest(unittest.TestCase):
    capacity=100

    def setUp(self):
        self.worstFit = WorstFitAlgorithm()
        self.bins=list()
        self.bins.append(Bin(WorstFitAlgorithmTest.capacity))
        self.item80 = Item(80)
        self.item40 = Item(40)
        self.item10 = Item(10)
        
    def test_findBin(self):
        capacity = WorstFitAlgorithmTest.capacity
        
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

        b = self.worstFit.findBin(self.item10, capacity, self.bins)
        b.addItem(self.item10)

        self.assertEqual(80, b80.loading())
        self.assertEqual(40, b40.loading())
        self.assertEqual(20, b10.loading())
        self.assertEqual(3, len(self.bins))

    def test_no_fitting_bin(self):
        capacity = WorstFitAlgorithmTest.capacity
                
        b80 = Bin(capacity)
        b80.addItem(self.item80)

        self.bins[0] = b80

        b = self.worstFit.findBin(self.item40, capacity, self.bins)
        b.addItem(self.item40)

        self.assertEqual(80, b80.loading())
        self.assertEqual(2, len(self.bins))
        self.assertEqual(40, self.bins[1].loading())
