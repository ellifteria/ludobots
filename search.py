import os

for i in range(5):
    os.system("python generate.py")

    from simulation import Simulation

    simulation = Simulation()
    simulation.run()