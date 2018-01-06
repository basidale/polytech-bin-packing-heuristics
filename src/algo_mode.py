from simulation import Simulation
import os
from reader import ItemReader
from algorithms import *
from xml_generator import XMLGenerator

class AlgoMode:
    def __init__(self, xml=False):
        self.xml = xml
    
    def start(self, examples):
        sourcePath = os.path.dirname(os.path.realpath(__file__))
        
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
                outputFileName = algorithm.getName().replace(' ', '-') + '-' + exampleName + '.xml'
                outputFileName = outputFileName.lower()
                outputFilePath = sourcePath + '/../simulations/' + outputFileName
                simulation = Simulation(capacity, list(items), algorithm)

                if self.xml:
                    generator = XMLGenerator(simulation)
                    generator.generate(outputFilePath)
                else:
                    simulation.run()

    
