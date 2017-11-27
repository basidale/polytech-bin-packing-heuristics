class Item:
    size = 0

    def __init__(self, size):
        self.size = size

    def isFittingInto(self, container):
        return (container.loading() + self.size) <= container.capacity
    
    def __str__(self):
        print(self.size)
