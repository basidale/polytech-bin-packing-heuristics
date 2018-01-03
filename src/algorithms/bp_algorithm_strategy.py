from abc import ABCMeta, abstractmethod

class IBinPackingAlgorithmStrategy(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def getName():
        return
    
    @abstractmethod
    def findBin(self, item, capacity, bins, bst):
        return
        
    @abstractmethod
    def getBins(self):
        return
    
