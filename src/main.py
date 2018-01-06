from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader
from xml_generator import XMLGenerator
from stat_scenario import StatExecutionScenario
from stat_mode import StatMode
from algo_mode import AlgoMode
from random import randint
import argparse
import os 

            
if __name__ == '__main__':
    sourcePath = os.path.dirname(os.path.realpath(__file__))

    parser = argparse.ArgumentParser(description='TODO: write description')
    parser.add_argument('--run',
                        nargs=1,
                        required=True,
                        choices=[ 'ALGO', 'STAT', 'XML'],
                        help='TODO:')
    
    args = parser.parse_args()

    examples = [ 'exemple100.txt', 'exemple500.txt', 'exemple1000.txt' ]
    
    mode = None
    
    if args.run[0] == 'ALGO':
        mode = AlgoMode().start(examples)
    elif args.run[0] == 'STAT':
        mode = StatMode().start()
    # TODO: Supprimer pour le rendu
    elif args.run[0] == 'XML':
        mode = AlgoMode(True).start(examples)
    else:
        pass

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






