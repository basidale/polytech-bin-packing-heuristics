from functools import total_ordering

@total_ordering
class Bin:
    counter = 0
    
    def __init__(self, capacity):
        Bin.counter += 1

        self.number = Bin.counter
        self.itemList = list()
        self.capacity = capacity

    def addItem(self, item):
        self.itemList.append(item)
    
    def loading(self):
        loading = 0
        for item in self.itemList:
            loading += item.size
        return loading
    
    def __str__(self):
        binLoading = self.loading()
        percentage = (binLoading / self.capacity) * 100
        percentage = round(percentage, 2)
        
        return str(binLoading) + ' / ' + str(self.capacity) + ' [' + str(percentage) + '%]'
    
    def __lt__(self, other):
        return self.number < other.number
    
    def __eq__(self, other):
        return self.number == other.number

