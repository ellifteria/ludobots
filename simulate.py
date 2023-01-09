import os

os.system("python generate.py")

import pybullet as pblt
import pybullet_data
import time

import pyrosim_modded.pyrosim_modded as pyrosim

physicsClient = pblt.connect(pblt.GUI)

pblt.setAdditionalSearchPath(pybullet_data.getDataPath())

pblt.setGravity(0,0,-9.8)

plane_id = pblt.loadURDF("plane.urdf")

robot_id = pblt.loadURDF("body.urdf")

pblt.loadSDF("box.sdf")

pyrosim.Prepare_To_Simulate(robot_id)

while True:
    pblt.stepSimulation()

    backleg_touch = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")

    print(backleg_touch)

    time.sleep(1/60)

pblt.disconnect()