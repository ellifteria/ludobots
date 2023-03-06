import os

os.system("python generate.py")
os.system("bash file.copier.sh")

import pybullet as p
import pybullet_data
import time
from timeit import default_timer as timer

def simulate():
    physicsClient = p.connect(p.DIRECT)

    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    p.setGravity(0,0,-9.8)

    planeID = p.loadURDF("plane.urdf")

    robotID = p.loadURDF("body.urdf")

    p.loadSDF("box.sdf")

    for i in range(10000):
        p.stepSimulation()
        time.sleep(0.1/60)

    p.disconnect()

def main():
    for i in range(10):
        simulate()

if __name__ == "__main__":
    start_time = timer()
    main()
    end_time = timer()
    elapsed_time = end_time - start_time
    print('execution time:', elapsed_time, 'seconds')