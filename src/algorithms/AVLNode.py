from heapq import heappush, heappop
from functools import total_ordering

class AVLNode:
    def __init__(self, parent, key, left = None, right = None):
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = 0
        self.height = 0
        self.size = 1
        self.key = key
        self.dataQueue = []
        self.minLoading = key.loading()
        
    def isLeaf(self):
        return self.left is None and self.right is None

    def isRoot(self):
        return self.parent is None

    def addKey(self, key):
        if key < self.key:
            heappush(self.dataQueue, self.key)
            self.key = key
        elif key > self.key:
            heappush(self.dataQueue, key)

    def updateKey(self):
        self.key = heappop(self.dataQueue)
    
    def addLoading(self, key):
        if key.loading() < self.minLoading:
            self.minLoading = key.loading()
    
    def updateLoading(self):
        leftLoading = self.left.minLoading if self.left is not None else 0
        rightLoading = self.right.minLoading if self.right is not None else 0
        self.minLoading = - min(- leftLoading, - rightLoading, - self.key.loading())
    
    def sizeOfLeftSubtree(self):
        if self.left is None:
            return 0
        return self.left.size
            
    def display(self, level=0):
        print('  ' * level + repr(self.key.loading()) + ' (' + repr(self.key.number) + ')' + ' [ ' + str(self.minLoading) + ' ]')
        if self.left is not None:
            self.left.display(level + 1)
        else:
            print('  ' * (level + 1) + '*')
        if self.right is not None:
            self.right.display(level + 1)
        else:
            print('  ' * (level + 1) + '*')
    
    def qtData(self):
        return len(self.dataQueue) + (0 if self.key is None else 1)

    def values(self):
        values = [ self.key ]
        values.extend(self.dataQueue)

        return sorted(values)

    
