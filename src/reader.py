import csv
from item import Item

class ItemReader:
    def __init__(self, inputFilePath):
        self.inputFilePath = inputFilePath

    def readItems(self):
        itemList = list()

        with open(self.inputFilePath) as inputFile:
            reader = csv.reader(inputFile)
            row = next(reader)
            for value in row:
                itemList.append(Item(int(value)))

        return itemList

