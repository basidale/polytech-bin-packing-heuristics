from simulation import Simulation
from item import Item
from algorithms import *
from reader import ItemReader
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
    
    if args.run[0] == 'ALGO':
        mode = AlgoMode().start(examples)
    elif args.run[0] == 'STAT':
        mode = StatMode().start()
    else:
        pass
