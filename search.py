import os

from simulation import Simulation

for i in range(5):
    os.system("python generate.py")

    simulation = Simulation()
    simulation.run()
    del simulation