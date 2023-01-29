import os

from simulation import Simulation
from hillclimber import HillClimber

hc = HillClimber()
hc.evolve()

# for i in range(5):
#     os.system("python generate.py")

#     simulation = Simulation()
#     simulation.run()
#     del simulation