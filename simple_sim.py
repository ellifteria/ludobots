import os

os.system("python simple_sim_gen.py")

import pybullet as pblt
import pybullet_data
import time
import numpy as np

import pyrosim_modded.pyrosim_modded as pyrosim

physicsClient = pblt.connect(pblt.GUI)

pblt.setAdditionalSearchPath(pybullet_data.getDataPath())

pblt.setGravity(0,0,-9.8)

plane_id = pblt.loadURDF("plane.urdf")

pblt.loadSDF("terrain.sdf")

robot_id = pblt.loadURDF("body.urdf")

num_iterations = 1000

pyrosim.Prepare_To_Simulate(robot_id)

for i in range(num_iterations):
    pblt.stepSimulation()
    time.sleep(0.05/60)

pblt.disconnect()