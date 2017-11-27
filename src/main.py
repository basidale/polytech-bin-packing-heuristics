from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader

# TODO: Check python 3 standards
if __name__ == '__main__':
    capacity = 15
    inputFilePath = '../res/data.csv'
    itemList = ItemReader(inputFilePath).readItems()

    #algorithm = next_fit_algorithm.NextFitAlgorithm()
    #algorithm = FirstFitAlgorithm()
    #algorithm = WorstFitAlgorithm()
    algorithm = AlmostWorstFitAlgorithm()
    simulation = Simulation(capacity, itemList, algorithm)
    simulation.run()
