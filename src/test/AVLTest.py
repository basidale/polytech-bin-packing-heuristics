import unittest
from random import shuffle
from bin import Bin
from item import Item
from algorithms.AVLTree import *

# TODO: Check balance in tests
class AVLTest(unittest.TestCase):
    capacity = 100
    
    def setUp(self):
        self.bin10 = Bin(AVLTest.capacity)
        self.bin10.addItem(Item(10))
        
        self.bin50 = Bin(AVLTest.capacity)
        self.bin50.addItem(Item(50))
        
        self.bin100 = Bin(AVLTest.capacity)
        self.bin100.addItem(Item(100))

        self.bin50b = Bin(AVLTest.capacity)
        self.bin50b.addItem(Item(50))

        self.bin50c = Bin(AVLTest.capacity)
        self.bin50c.addItem(Item(50))

    
    def test_insert(self):
        tree = AVLTree(key=lambda x : x.loading())

        tree.insert(self.bin50b)
        self.assertEqual(tree.root.key, self.bin50b)

        tree.insert(self.bin10)
        self.assertEqual(tree.root.left.key, self.bin10)

        tree.insert(self.bin100)
        self.assertEqual(tree.root.right.key, self.bin100)

        # Asserts older is returned
        tree.insert(self.bin50)
        self.assertEqual(tree.root.key, self.bin50)

        tree.insert(self.bin50b)
        self.assertEqual(tree.root.key, self.bin50)

    def test_insert2(self):
        loadings = [ 85, 12 , 35 , 96 , 34, 13, 7, 2, 21, 72, 9, 3, 25, 43 ]
        bins = [ AVLTest.binOfLoading(x) for x in loadings ]
        tree = AVLTree(key=lambda x : x.loading())
        
        for index, bin_ in enumerate(bins):
            tree.insert(bin_)
            expected = sorted(bins[:index + 1], key=lambda x : x.loading())
            self.assertEqual(expected, tree.values())
            self.checkNodeBalanced(tree.root)

        bin_ = AVLTest.binOfLoading(85)
        tree.insert(bin_)
        bins.append(bin_)

        expected = sorted(bins, key=lambda x : x.loading())
        self.assertEqual(expected, tree.values())

    def test_remove(self):
        loadings = [ 85, 12 , 35 , 96 , 34, 13, 7, 2, 21, 72, 9, 3, 25, 43 ]
        bins = [ AVLTest.binOfLoading(x) for x in loadings ]
        tree = AVLTree(key=lambda x : x.loading())
        
        for bin_ in bins:
            tree.insert(bin_)

        removed = [ bins[0], bins[2], bins[4], bins[10], bins[11] ]

        for _bin in removed:
            bins.remove(_bin)
            tree.remove(_bin)

        values = tree.values()
        self.assertEqual(sorted(bins, key=lambda x: x.loading()), values)
        self.checkNodeBalanced(tree.root)            

        for _bin in bins:
            tree.remove(_bin)

        self.assertEqual(0, len(tree.values()))

        # Asserts older is returned
        tree.insert(self.bin50)
        self.assertEqual(tree.root.key, self.bin50)

        tree.insert(self.bin50b)
        self.assertEqual(tree.root.key, self.bin50)

        tree.remove(self.bin50)
        self.assertEqual(tree.root.key, self.bin50b)
        
    def checkNodeBalanced(self, node):
        if node is None:
            return
        
        leftHeight = AVLTest.height(node.left)
        rightHeight = AVLTest.height(node.right)
        diff = abs(leftHeight - rightHeight)
        self.assertLessEqual(diff, 1)
        
        self.checkNodeBalanced(node.left)
        self.checkNodeBalanced(node.right)
    
    def checkSize(self, node):
        if node is None:
            return

        expected = 1
        expected += node.right.size if node.right is not None else 0
        expected += node.left.size if node.left is not None else 0
        self.assertEqual(expected, node.size)
        
        self.checkNodeBalanced(node.left)
        self.checkNodeBalanced(node.right)
                
    def test_node_with_multiple_keys(self):
        node = AVLNode(None, self.bin50b)
        self.assertEqual(self.bin50b, node.key)

        node.addKey(self.bin50)
        self.assertEqual(self.bin50, node.key)

        node.addKey(self.bin50c)
        self.assertEqual(self.bin50, node.key)

        node.updateKey()
        self.assertEqual(self.bin50b, node.key)
        
        node.updateKey()
        self.assertEqual(self.bin50c, node.key)
        
    def test_size(self):
        tree = AVLTree(key=lambda x : x.loading())

        bin60 = AVLTest.binOfLoading(60)
        bin50 = AVLTest.binOfLoading(50)
        bin70 = AVLTest.binOfLoading(70)
        bin80 = AVLTest.binOfLoading(80)
        bin90 = AVLTest.binOfLoading(90)
        bin75 = AVLTest.binOfLoading(75)
        
        tree.insert(bin60)
        self.assertEqual(1, tree.root.size)
        
        tree.insert(bin50)
        self.assertEqual(2, tree.root.size)
        self.assertEqual(1, tree.root.left.size)
        
        tree.insert(bin70)
        self.assertEqual(3, tree.root.size)
        self.assertEqual(1, tree.root.left.size)
        self.assertEqual(1, tree.root.right.size)
        
        tree.insert(bin80)
        self.assertEqual(4, tree.root.size)
        self.assertEqual(1, tree.root.left.size)
        self.assertEqual(2, tree.root.right.size)
        self.assertEqual(1, tree.root.right.right.size)

        tree.insert(bin90)
        self.assertEqual(5, tree.root.size)
        self.assertEqual(1, tree.root.left.size)
        self.assertEqual(3, tree.root.right.size)
        self.assertEqual(1, tree.root.right.left.size)
        self.assertEqual(1, tree.root.right.right.size)
        
        tree.insert(bin75)
        self.assertEqual(6, tree.root.size)
        self.assertEqual(2, tree.root.left.size)
        self.assertEqual(1, tree.root.left.left.size)
        self.assertEqual(3, tree.root.right.size)
        self.assertEqual(1, tree.root.right.left.size)
        self.assertEqual(1, tree.root.right.right.size)

    def test_size2(self):
        loadings = [ 85, 12 , 35 , 96 , 34, 13, 7, 2, 21, 72, 9, 3, 25, 43 ]
        
        tree = AVLTree(key=lambda x : x.loading())        

        for index, loading in enumerate(loadings):
            tree.insert(AVLTest.binOfLoading(loading))
            self.checkSize(tree.root)

    def test_minLoading(self):
        loadings = [ 85, 12 , 35 , 96 , 34, 13, 7, 2, 21, 72, 9, 3, 25, 43 ]
        bins = [ AVLTest.binOfLoading(loading) for loading in loadings ]
        tree = AVLTree()

        for bin_ in bins:
            tree.insert(bin_)
            self.checkMinLoading(tree.root)
            
        removed = [ bins[0], bins[2], bins[4], bins[10], bins[11] ]

        for _bin in removed:
            tree.remove(_bin)
            self.checkMinLoading(tree.root)
            
    def test_select(self):
        loadings = [ 85, 12 , 35 , 96 , 34, 13, 7, 2, 21, 72, 9, 3, 25, 43 ]
        bins = list()
        tree = AVLTree(key=lambda x : x.loading())        

        for loading in loadings:
            bin_ = AVLTest.binOfLoading(loading)
            bins.append(bin_)
            tree.insert(bin_)

        bins.sort(key=lambda x : x.loading())
        for index, bin_ in enumerate(bins):
            self.assertEqual(bin_, tree.select(index))

    def checkMinLoading(self, node):
        if node is None:
            return False
        
        result = node.key.loading() == node.minLoading
        result |= self.containsLoading(node.left, node.minLoading)
        result |= self.containsLoading(node.right, node.minLoading)

        result &= self.checkMinLoading(node.left) 
        result &= self.checkMinLoading(node.right)
        
        return result
        
    def containsLoading(self, node, loading):
        if node is None:
            return False

        result = node.key.loading() == loading
        result |= self.containsLoading(node.left, loading)
        result |= self.containsLoading(node.right, loading)
        
        return result
        
    @staticmethod
    def height(node):
        if (node is None):
            return -1
        
        return 1 + max(AVLTest.height(node.left), AVLTest.height(node.right))

    @staticmethod
    def binOfLoading(loading):
        bin_ = Bin(AVLTest.capacity)
        bin_.addItem(Item(loading))
        return bin_

    
