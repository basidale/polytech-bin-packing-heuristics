from .AVLNode import *

class AVLTree:
    def __init__(self, key = None):
        self.root = None
        self.height = -1
        self.balance = 0

        if key is None:
            self.key = lambda x : x
        else:
            self.key = key
    
    def insert(self, key):
        if self.root is None:
            self.root = AVLNode(None, key)
            return
        
        parent = None
        current = self.root
        toLeft = False
        
        while current is not None:
            current.addLoading(key)
            if self._compare(current.key, key) == 0:
                current.addKey(key)
                return
            
            parent = current
            toLeft = self._compare(current.key, key) == 1
            current = current.left if toLeft else current.right
            parent.size += 1
            
            
        node = AVLNode(parent, key)
        
        if toLeft:
            parent.left = node
        else:
            parent.right = node

        self._rebalance(parent)
    
    def remove(self, key):
        node = self.find(key)

        if node is None:
            return False

        if node.qtData() > 1:
            node.updateKey()
        else:
            self._remove(node)

        while node is not None:
            if node.key.loading() == node.minLoading:
                node.updateLoading()
            node = node.parent
        
        return True

    def find(self, key):
        return self._find(key)

    def select(self, index):
        return self._select(self.root, index)

    def values(self):
        result = list()
        self._values(self.root, result)

        return result
        
    def display(self, level=0):
        print('tree: ')
        if self.root is None:
            print('empty tree')
        else:
            self.root.display()
        print('endtree')
    
    def _rebalance(self, node):
        self._updateBalance(node)
        
        if node.balance == -2:
            if self._heightOf(node.left.left) >= self._heightOf(node.left.right):
                node = self._rotateRight(node)
            else:
                node = self._rotateLeftThenRight(node)
        elif node.balance == 2:
            if self._heightOf(node.right.right) >= self._heightOf(node.right.left):
                node = self._rotateLeft(node)
            else:
                node = self._rotateRightThenLeft(node)
        
        if node.parent is not None:
            self._rebalance(node.parent)
        else:
            self.root = node
    
    def _rotateLeft(self, node):
        b = node.right
        b.parent = node.parent

        node.right = b.left
        
        if node.right is not None:
            node.right.parent = node
        
        b.left = node
        node.parent = b
        
        if b.parent is not None:
            if b.parent.right == node:
                b.parent.right = b
            else:
                b.parent.left = b
        
        self._updateBalance(node)
        self._updateBalance(b)

        node.size = 1
        node.size += node.left.size if node.left is not None else 0
        node.size += node.right.size if node.right is not None else 0

        b.size = 1
        b.size += b.left.size if b.left is not None else 0
        b.size += b.right.size if b.right is not None else 0

        b.updateLoading()
        node.updateLoading()
        
        return b

    def _rotateRight(self, node):
        b = node.left;
        b.parent = node.parent;
 
        node.left = b.right;
 
        if node.left is not None:
            node.left.parent = node;
 
        b.right = node;
        node.parent = b;
 
        if b.parent is not None:
            if b.parent.right == node:
                b.parent.right = b;
            else:
                b.parent.left = b;

        self._updateBalance(node)
        self._updateBalance(b)

        node.size = 1
        node.size += node.left.size if node.left is not None else 0
        node.size += node.right.size if node.right is not None else 0

        b.size = 1
        b.size += b.left.size if b.left is not None else 0
        b.size += b.right.size if b.right is not None else 0
        
        return b
    
    def _rotateLeftThenRight(self, node):
        node.left = self._rotateLeft(node.left);
        return self._rotateRight(node);
 
    def _rotateRightThenLeft(self, node):
        node.right = self._rotateRight(node.right);
        return self._rotateLeft(node);

    # TODO: Move to Node
    def _updateBalance(self, node):
        self._updateHeight(node)
        node.balance = self._heightOf(node.right) - self._heightOf(node.left)
    
    def _updateHeight(self, node):
        node.height = 1 + max(self._heightOf(node.left), self._heightOf(node.right))
    
    def _remove(self, node):
        if node.isLeaf():
            if node.isRoot():
                self.root = None
            else:
                parent = node.parent
                
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                    
                self._rebalance(parent)
            return
        elif not node.isRoot():
            node.parent.size -= 1
        
        if node.left is not None:
            child = node.left
            while child.right is not None:
                child = child.right
            node.key = child.key
            self._remove(child)
        else:
            child = node.right
            while child.left is not None:
                child = child.left
            node.key = child.key
            self._remove(child)

            
    def _find(self, key, remove=False):
        current = self.root

        while current is not None and current.key is not key:
            if self._compare(current.key, key) == -1:
                current = current.right
            else:
                current = current.left
        
        return current

    
    def _select(self, node, index):
        if node is None:
            return None
        
        size = node.sizeOfLeftSubtree()

        if index == size:
            return node.key
        elif index < size:
            return self._select(node.left, index)
        else:
            return self._select(node.right, index - (size + 1))
    
    def _heightOf(self, node):
        if node is None:
            return -1
        return node.height
        
    def _values(self, node, result):
        if node is None:
            return

        self._values(node.left, result)
        result.extend(node.values())
        self._values(node.right, result)

    def _compare(self, key1, key2, key = None):
        if key is None:
            key = self.key

        key1 = key(key1)
        key2 = key(key2)

        if key1 < key2:
            return -1
        elif key1 > key2:
            return 1

        return 0
    
    def _createNode(self, parent, key, left = None, right = None):
        node = AVLNode(parent, key, left, right)
        node.setKeyProperty(self.key)
        
        return node
