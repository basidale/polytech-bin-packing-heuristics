from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader
from xml_generator import XMLGenerator
import os 

if __name__ == '__main__':
    sourcePath = os.path.dirname(os.path.realpath(__file__))
        
    examples = [ 'exemple100.txt', 'exemple500.txt', 'exemple1000.txt' ]

    for example in examples:
        exampleName = example.split('.')[0]
        inputFilePath = sourcePath + '/../res/' + example
        items, capacity = ItemReader(inputFilePath).readItems()

        algorithms = [ FirstFitAlgorithm(),
                       NextFitAlgorithm(),
                       WorstFitAlgorithm(),
                       AlmostWorstFitAlgorithm(),
                       BestFitAlgorithm() ]
        
        for algorithm in algorithms:
            print(example + " " + algorithm.NAME)
            outputFileName = algorithm.NAME.replace(' ', '-') + '-' + exampleName + '.xml'
            outputFileName = outputFileName.lower()
            outputFilePath = sourcePath + '/../simulations/' + outputFileName
            simulation = Simulation(capacity, list(items), algorithm)
            simulation.run()
            generator = XMLGenerator(simulation)
            generator.generate(outputFilePath)

