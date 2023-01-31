import sys

pybullet_method = sys.argv[1]
solution_id = sys.argv[2]

from simulation import Simulation

simulation = Simulation(pybullet_method, solution_id)
simulation.run()
simulation.get_fitness()