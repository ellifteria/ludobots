import numpy as np
import pyrosim_modded.pyrosim_modded as pyrosim
import pybullet as pblt
from datetime import datetime

import constants as c

class Motor:

    def __init__(self, joint_name):
        self.joint_name = joint_name
        self.max_force = 25

    def set_value(self, robot, desired_angle):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex= robot.id,
                jointName= self.joint_name,
                controlMode= pblt.POSITION_CONTROL,
                targetPosition= desired_angle * c.motor_joint_range,
                maxForce= self.max_force
            )
    
    def save_values(self):
        with open("./data/{}_sensor_{}.npy".format(datetime.now().strftime('%Y%m%d_%H%M'), self.joint_name), 'wb') as f:
            np.save(f, self.values)
            f.close()
