class Item:
    size = 0

    def __init__(self, size):
        self.size = size

    def fitsInto(self, container):
        return (container.loading() + self.size) <= container.capacity
    
    def __str__(self):
        return str(self.size)

    def __repr__(self):
        return self.__str__()
