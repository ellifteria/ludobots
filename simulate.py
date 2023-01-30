import sys

pybullet_method = sys.argv[1]

from simulation import Simulation

simulation = Simulation(pybullet_method)
simulation.run()
simulation.get_fitness()