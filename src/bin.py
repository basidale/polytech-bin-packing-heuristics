from functools import total_ordering

@total_ordering
class Bin:
    def __init__(self, capacity):
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
        return self.loading() < other.loading()
    
    def __eq__(self, other):
        return loading() == other.loading()

