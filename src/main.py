from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader

# TODO: Check python 3 standards
if __name__ == '__main__':
    # TODO: Put in file
    #inputFilePath = '../res/data.csv'
    inputFilePath = '../res/exemple100.txt'
    items, capacity = ItemReader(inputFilePath).readItems()
    
    #algorithm = next_fit_algorithm.NextFitAlgorithm()
    #algorithm = FirstFitAlgorithm()
    #algorithm = WorstFitAlgorithm()
    #algorithm = AlmostWorstFitAlgorithm()
    algorithm = BestFitAlgorithm()
    simulation = Simulation(capacity, items, algorithm)
    simulation.run()
