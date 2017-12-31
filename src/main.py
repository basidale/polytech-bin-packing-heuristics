from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader
from xml_generator import XMLGenerator
from random import randint
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
    


    """var = int(input('Entrez le nombre dexemples de tests:'))
    binSize = input('Entrez la taille des bins :')
    maxNumberOfPack = int(input('Entrez le nombre maximal de paquets :'))
    minNumberOfPack = int(input('Entrez la nombre minimal de paquets :'))

    for i in range(var):
        f = open(sourcePath + '/../res/exemple' + str(i), 'w')
        f.write('Taille bin\n')
        f.write(binSize + '\n')
        f.write('Objets\n')
        numberOfPack = randint(minNumberOfPack, maxNumberOfPack)
        for j in range(numberOfPack):
           packSize = randint(1, int(binSize))
           f.write(str(packSize))
           if j < numberOfPack - 1:
               f.write(', ')
        f.write('.')
        f.close()"""






