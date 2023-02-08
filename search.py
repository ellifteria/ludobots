import argparse
from ludofae1 import ludoFAE1
from ludofae2 import ludoFAE2

parser = argparse.ArgumentParser(
    prog = 'search.py',
    description = 'Performs a search for an optimizied neural network weight set for a simulated robot using FAEry Algorithms')
parser.add_argument('-m', '--method', choices=['ludoFAE1', 'ludoFAE2'], default='ludoFAE1')

args = parser.parse_args()

if args.method == 'ludoFAE1':
    evolutionary_algorithm = ludoFAE1()
elif args.method == 'ludoFAE2':
    evolutionary_algorithm = ludoFAE2()
else:
    exit()


evolutionary_algorithm.evolve()

exit()