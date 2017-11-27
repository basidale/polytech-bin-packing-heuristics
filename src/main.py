from simulation import Simulation
from item import Item
from algorithms import *


# TODO: Check python 3 standards
if __name__ == '__main__':
    capacity = 15
    itemList = list()
    
    # Put in a file
    # itemList.append(Item(4))
    # itemList.append(Item(12))
    # itemList.append(Item(9))
    # itemList.append(Item(2))
    # itemList.append(Item(5))
    # itemList.append(Item(11))
    ## Worst fit data set
    itemList.append(Item(15))
    itemList.append(Item(12))
    itemList.append(Item(12))
    itemList.append(Item(1))
    itemList.append(Item(5))
    itemList.append(Item(6))
    itemList.append(Item(12))
    # end
    
    #algorithm = next_fit_algorithm.NextFitAlgorithm()
    #algorithm = FirstFitAlgorithm()
    #algorithm = WorstFitAlgorithm()
    algorithm = AlmostWorstFitAlgorithm()
    simulation = Simulation(capacity, itemList, algorithm)
    simulation.run()
