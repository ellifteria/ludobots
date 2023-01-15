import os

os.system("python generate.py")

from simulation import Simulation

simulation = Simulation()
simulation.run()