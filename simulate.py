import os

os.system("python generate.py")

import pybullet as pblt
import pybullet_data
import time
import numpy as np

import pyrosim_modded.pyrosim_modded as pyrosim

import constants as c

# physicsClient = pblt.connect(pblt.GUI)

# pblt.setAdditionalSearchPath(pybullet_data.getDataPath())

# pblt.setGravity(0, 0, -9.8)

# plane_id = pblt.loadURDF("plane.urdf")

# robot_id = pblt.loadURDF("body.urdf")

# pblt.loadSDF("box.sdf")

# backleg_sensor_vals = np.zeros(c.num_iterations)
# frontleg_sensor_vals = np.zeros(c.num_iterations)

# front_motor_vals = c.front_amplitude*np.sin(c.front_phase_offset + c.front_frequency*np.linspace(0, 2*np.pi, c.num_iterations))
# back_motor_vals = c.back_amplitude*np.sin(c.back_phase_offset + c.back_frequency*np.linspace(0, 2*np.pi, c.num_iterations))

# with open("./data/backleg_motor_vals.npy", 'wb') as f:
#     np.save(f, back_motor_vals)
#     f.close()
# with open("./data/frontleg_motor_vals.npy", 'wb') as f:
#     np.save(f, front_motor_vals)
#     f.close()

# pyrosim.Prepare_To_Simulate(robot_id)

# for i in range(c.num_iterations):
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex= robot_id,
#         jointName= "torso_backleg",
#         controlMode= pblt.POSITION_CONTROL,
#         targetPosition= front_motor_vals[i],
#         maxForce= 15
#     )

#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex= robot_id,
#         jointName= "torso_frontleg",
#         controlMode= pblt.POSITION_CONTROL,
#         targetPosition= back_motor_vals[i],
#         maxForce= 15
#     )

#     pblt.stepSimulation()

#     backleg_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
#     frontleg_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
#     print(backleg_sensor_vals[i])
#     print(frontleg_sensor_vals[i])

#     time.sleep(0.05/60)

# with open("./data/backleg_sensor_vals.npy", 'wb') as f:
#     np.save(f, backleg_sensor_vals)
#     f.close()
# with open("./data/frontleg_sensor_vals.npy", 'wb') as f:
#     np.save(f, frontleg_sensor_vals)
#     f.close()

# pblt.disconnect()

from simulation import Simulation

simulation = Simulation()
simulation.run()