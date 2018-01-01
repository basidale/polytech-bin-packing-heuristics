from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader
from xml_generator import XMLGenerator
from random import randint
import argparse
import os 

def executeAll(examples):
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
            #generator = XMLGenerator(simulation)
            #generator.generate(outputFilePath)

# TODO: Supprimer pour le rendu
def generateXML(examples):
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
            generator = XMLGenerator(simulation)
            generator.generate(outputFilePath)
            
if __name__ == '__main__':
    sourcePath = os.path.dirname(os.path.realpath(__file__))

    parser = argparse.ArgumentParser(description='TODO: write description')
    parser.add_argument('--run',
                        nargs=1,
                        required=True,
                        choices=[ 'ALGO', 'XML'],
                        help='TODO:')
    
    args = parser.parse_args()

    
    if args.run[0] == 'ALGO':
        examples = [ 'exemple100.txt', 'exemple500.txt', 'exemple1000.txt' ]
        executeAll(examples)
    # TODO: Supprimer pour le rendu
    elif args.run[0] == 'XML':
        examples = [ 'exemple100.txt', 'exemple500.txt', 'exemple1000.txt' ]
        generateXML(examples)
    else:
        raise 

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






