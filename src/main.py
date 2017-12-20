from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader
from xml_generator import XMLGenerator
import os 

# TODO: Check python 3 standards
if __name__ == '__main__':
    filePath = os.path.dirname(os.path.realpath(__file__))
    
    # TODO: Put in file
    #inputFilePath = '../res/data.csv'
    inputFilePath = filePath + '/../res/exemple100.txt'
    items, capacity = ItemReader(inputFilePath).readItems()
    
    firstFitAlgorithm = FirstFitAlgorithm()
    worstFitAlgorithm = WorstFitAlgorithm()
    almostWorstFitAlgorithm = AlmostWorstFitAlgorithm()
    nextFitAlgorithm = NextFitAlgorithm()
    bestFitAlgorithm = BestFitAlgorithm()

    algorithms = [ firstFitAlgorithm,
                   nextFitAlgorithm,
                   worstFitAlgorithm,
                   almostWorstFitAlgorithm,
                   bestFitAlgorithm ]
    
    for algorithm in algorithms:
        outputFileName = algorithm.NAME.replace(' ', '-')
        outputFileName = outputFileName.lower()
        outputFileName = filePath + '/../simulations/' + outputFileName + '-example100.xml'
        
        simulation = Simulation(capacity, list(items), algorithm)
        generator = XMLGenerator(simulation)        
        generator.generate(outputFileName)

