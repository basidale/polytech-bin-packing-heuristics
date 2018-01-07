from simulation import Simulation
import os
from reader import ItemReader
from algorithms import *

class AlgoMode:
    def start(self, examples):
        sourcePath = os.path.dirname(os.path.realpath(__file__))
        
        for example in examples:
            exampleName = example.split('.')[0]
            inputFilePath = sourcePath + '/../examples/' + example
            items, capacity = ItemReader(inputFilePath).readItems()
            
            algorithms = [ FirstFitAlgorithm(),
                           NextFitAlgorithm(),
                           WorstFitAlgorithm(),
                           AlmostWorstFitAlgorithm(),
                           BestFitAlgorithm() ]
        
            for algorithm in algorithms:
                simulation = Simulation(capacity, list(items), algorithm)

                simulation.run()

    
