import os

from simulation import Simulation
from parallel_hillclimber import ParallelHillClimber

phc = ParallelHillClimber()
phc.evolve()

exit()

# for i in range(5):
#     os.system("python generate.py")

#     simulation = Simulation()
#     simulation.run()
#     del simulation