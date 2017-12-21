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
            # Removes special characters '\n' at the end of each line
            content = [x.strip() for x in content]
            # Removes final dot in item list
            content[ITEMS_INDEX] = content[ITEMS_INDEX][:-1]
        
        capacity = int(content[CAPACITY_INDEX])
        
        # Fill the item list with list of item size under string format
        items = [ Item(int(item)) for item in content[ITEMS_INDEX].split(', ') ]

        return items, capacity
