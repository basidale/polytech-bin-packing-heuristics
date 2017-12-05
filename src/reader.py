from item import Item

CAPACITY_INDEX = 1
ITEMS_INDEX = 3


# TODO: Handle exceptions:
# - Incorrect file format
class ItemReader:
    
    def __init__(self, inputFilePath):
        self.inputFilePath = inputFilePath

    def readItems(self):
        content = list()
        
        with open(self.inputFilePath) as inputFile:
            content = inputFile.readlines()
            content = [x.strip() for x in content]
            content[ITEMS_INDEX] = content[ITEMS_INDEX][:-1]

        # Removes special characters '\n' at the end of each line
        capacity = int(content[CAPACITY_INDEX])
        
        items = [ Item(int(item)) for item in content[ITEMS_INDEX].split(', ') ]

        return items, capacity
