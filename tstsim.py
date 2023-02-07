
import pybullet as p
import pybullet_data
import time
import numpy as np

import pyrosim_modded.pyrosim_modded as pyrosim

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

num_iterations = 1000

terrainShape = p.createCollisionShape(shapeType = p.GEOM_HEIGHTFIELD, meshScale=[.5,.5,2.5],fileName = "heightmaps/ground0.txt", heightfieldTextureScaling=128)
terrain  = p.createMultiBody(0, terrainShape)
p.resetBasePositionAndOrientation(terrain,[0,0,0], [0,0,0,1])


# pyrosim.Prepare_To_Simulate(robot_id)

for i in range(num_iterations):
    p.stepSimulation()
    time.sleep(0.05/60)

p.disconnect()