import argparse
from p_fae1 import P_FAE_1
from f_fae1 import F_FAE_1

parser = argparse.ArgumentParser(
    prog = 'search.py',
    description = 'Performs a search for an optimizied neural network weight set for a simulated robot using FAEry Algorithms')
parser.add_argument('-m', '--method', choices=['p_fae_1', 'f_fae_1'], default='p_fae_1')

args = parser.parse_args()

if args.method == 'p_fae_1':
    evolutionary_algorithm = P_FAE_1()
elif args.method == 'f_fae_1':
    evolutionary_algorithm = F_FAE_1()
else:
    exit()


evolutionary_algorithm.evolve()

exit()