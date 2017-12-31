class BinBST:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, bin_):
        self.root = self._insert(self.root, bin_)
        self.size += 1
    
    def _insert(self, node, bin_):
        if node is None:
            node = self.Node(bin_)

        elif bin_.loading() < node.data.loading():
            node.left = self._insert(node.left, bin_)
            node.left.parent = node
        elif bin_.loading() > node.data.loading():
            node.right = self._insert(node.right, bin_)
            node.right.parent = node
        else:
            if bin_ < node.data:
                node = self.Node(bin_)
                
        return node

    def display(self):
        print('[')
        self._display(self.root)
        print(']')
    
    def _display(self, node):
        if node.left is not None:
            self._display(node.left)
        print(node.data)
        if node.right is not None:
            self._display(node.right)

            
    def removeMin(self):
        if (self.root.left is None):
            data = self.root.data
            self.root = None
            return data

        node = self._removeMin(self.root).data

        return node
        
    def _removeMin(self, node):
        if node.left is not None:
            return self._removeMin(node.left)

        if node.right is None:
            node.parent.left = None
        else:
            node.parent.left = self._removeMin(node.right)
            
        return node

    
    class Node:
        def __init__(self, data, right = None, left = None):
            self.data = data
            self.right = right
            self.left = left
            self.parent = None
        

