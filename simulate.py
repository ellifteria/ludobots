import os

os.system("python generate.py")

import pybullet as pblt
import pybullet_data
import time
import numpy as np

import pyrosim_modded.pyrosim_modded as pyrosim

physicsClient = pblt.connect(pblt.GUI)

pblt.setAdditionalSearchPath(pybullet_data.getDataPath())

pblt.setGravity(0,0,-9.8)

plane_id = pblt.loadURDF("plane.urdf")

robot_id = pblt.loadURDF("body.urdf")

pblt.loadSDF("box.sdf")

time_quit = True
num_iterations = 500
iteration = 0
backleg_sensor_vals = np.zeros(num_iterations)
frontleg_sensor_vals = np.zeros(num_iterations)

pyrosim.Prepare_To_Simulate(robot_id)

while True:
    if time_quit:
        if iteration >= num_iterations:
            break

    pblt.stepSimulation()

    if time_quit:
        backleg_sensor_vals[iteration] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
        frontleg_sensor_vals[iteration] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
        print(backleg_sensor_vals[iteration])
        print(frontleg_sensor_vals[iteration])
    
    else:
        backleg_sensor_val = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
        frontleg_sensor_val = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
        print(backleg_sensor_val)
        print(frontleg_sensor_val)
    
    if time_quit:
        iteration += 1

    time.sleep(0.05/60)

with open("./data/backleg_sensor_vals.npy", 'wb') as f:
    np.save(f, backleg_sensor_vals)
    f.close()
with open("./data/frontleg_sensor_vals.npy", 'wb') as f:
    np.save(f, frontleg_sensor_vals)
    f.close()

pblt.disconnect()