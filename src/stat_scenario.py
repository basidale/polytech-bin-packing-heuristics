from algorithms import *
from item import *
from simulation import Simulation
import random
import functools
import math

def dialog_normal_distribution(capacity):
    print('Mean : ')
    mean = int(input('> '))
    
    print('Standard deviation : ')
    std = int(input('> '))
        
    def rand_normal():
        a = math.floor(random.normalvariate(mean, std))
        while a < 0 or a > capacity:
            a = round(random.normalvariate(mean, std))
        return a
        
    return rand_normal

def dialog_uniform_distribution(capacity):
    print('Interval :')
    print('\'> a,b\' for interval [a,b] (default = 0,capacity)')
    
    interval = input('> ').split(',')
    if len(interval) == 1:
        a = 0
        b = capacity
    else:
        a = int(interval[0])
        b = int(interval[1])
    
    def rand_uniform():
        return random.randint(a, b)

    return rand_uniform
    
class StatExecutionScenario:
    heuristics = [ FirstFitAlgorithm(),
                   NextFitAlgorithm(),
                   WorstFitAlgorithm(),
                   AlmostWorstFitAlgorithm(),
                   BestFitAlgorithm() ]

    distributions = [
        ('Truncated normal distribution (approximation)', dialog_normal_distribution),
        ('Uniform distribution', dialog_uniform_distribution) ]
    
    def __init__(self):
        self.heuristic = 0
        self.capacity = 0
        self.numberOfItems = 0
        self.randomFunction = None
        self.items = []
    
    def execute(self):
        #numberOfSimulation = int(input('Nombre de simulations :'))
       
        #for i in range(numberOfSimulation):
        self.askForHeuristic()
        self.askForCapacity()
        self.askForNumberOfItems()
        self.askForDistribution()
        
        items=[]
        for i in range(self.numberOfItems):
            items.append(Item(self.randomFunction()))

        simulation = Simulation(self.capacity, items, self.heuristic)
        simulation.run()

    def askForHeuristic(self):
        choices = [ str(i) + "- " + h.getName() for i, h in enumerate(self.heuristics) ]
        choices = '\n  ' + '\n  '.join(choices)
        
        print('Heuristic :' + choices)
        index = int(input('> '))
        
        if index < 0 or index > len(self.heuristics) - 1:
            raise ValueError("Invalid heuristic choice : " + str(index))
        
        self.heuristic = self.heuristics[index]
    
    def askForCapacity(self):
        print('Bins capacity : ')
        self.capacity = int(input('> '))
        
        if self.capacity < 0:
            raise ValueError("Bins capacity must be positive")

    def askForNumberOfItems(self):
        print('Number of items : ')
        self.numberOfItems = int(input('> '))
        
        if self.numberOfItems < 0:
            raise ValueError("Number of items must be positive")

    def askForDistribution(self):
        choices = [ str(i) + "- " + d[0] for i, d in enumerate(self.distributions) ]
        choices = '\n  ' + '\n  '.join(choices)
        
        print('Distribution :' + choices)
        index = int(input('> '))
        
        if index < 0 or index > len(self.distributions) - 1:
            raise ValueError("Invalid distribution choice : " + str(index))
        
        dialog = self.distributions[index][1]
        self.randomFunction = dialog(self.capacity)
