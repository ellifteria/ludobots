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

num_iterations = 500
backleg_sensor_vals = np.zeros(num_iterations)
frontleg_sensor_vals = np.zeros(num_iterations)

pyrosim.Prepare_To_Simulate(robot_id)

for i in range(num_iterations):
    pyrosim.Set_Motor_For_Joint(
        bodyIndex= robot_id,
        jointName= "torso_backleg",
        controlMode= pblt.POSITION_CONTROL,
        targetPosition= np.pi*np.random.random()-np.pi/2,
        maxForce= 25
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex= robot_id,
        jointName= "torso_frontleg",
        controlMode= pblt.POSITION_CONTROL,
        targetPosition= np.pi*np.random.random()-np.pi/2,
        maxForce= 25
    )

    pblt.stepSimulation()

    backleg_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
    frontleg_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
    print(backleg_sensor_vals[i])
    print(frontleg_sensor_vals[i])

    time.sleep(0.05/60)

with open("./data/backleg_sensor_vals.npy", 'wb') as f:
    np.save(f, backleg_sensor_vals)
    f.close()
with open("./data/frontleg_sensor_vals.npy", 'wb') as f:
    np.save(f, frontleg_sensor_vals)
    f.close()

pblt.disconnect()