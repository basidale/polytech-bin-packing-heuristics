import unittest
from random import shuffle
from bin import Bin
from item import Item
from algorithms.bin_bst import BinBST


class BinBSTTest(unittest.TestCase):
    capacity = 100
    
    def test_insert(self):
        tree = BinBST()
        bin10 = Bin(BinBSTTest.capacity)
        bin10.addItem(Item(10))
        
        bin50 = Bin(BinBSTTest.capacity)
        bin50.addItem(Item(50))
        
        bin100 = Bin(BinBSTTest.capacity)
        bin100.addItem(Item(100))

        bin50b = Bin(BinBSTTest.capacity)
        bin50b.addItem(Item(50))

        tree.insert(bin50b)
        self.assertEqual(tree.root.data, bin50b)

        tree.insert(bin10)
        self.assertEqual(tree.root.left.data, bin10)

        tree.insert(bin100)
        self.assertEqual(tree.root.right.data, bin100)

        # Asserts older is conserved
        tree.insert(bin50)
        self.assertEqual(tree.root.data, bin50)

        tree.insert(bin50b)
        self.assertEqual(tree.root.data, bin50)
    
    def test_min(self):
        loadings = [ 85, 12, 35, 96, 34, 96, 12, 7, 12, 2, 21, 2, 9, 3 ]
        shuffle(loadings)
        
        tree = BinBST()        

        for loading in loadings:
            bin_ = Bin(BinBSTTest.capacity)
            bin_.addItem(Item(loading))
            tree.insert(bin_)

        minLoadingBin = tree.removeMin()
        self.assertEqual(2, minLoadingBin.loading())
            
        
