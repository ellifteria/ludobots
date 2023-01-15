import numpy as np
import pyrosim_modded.pyrosim_modded as pyrosim
import pybullet as pblt
from datetime import datetime

import constants as c

class Motor:

    def __init__(self, joint_name):
        self.joint_name = joint_name
        self.amplitude = c.amplitudes[joint_name]
        self.phase_offset = c.phase_offsets[joint_name]
        self.frequency = c.frequencies[joint_name]
        self.max_force = c.max_forces[joint_name]
        self.values = None
        self.prepare_to_act()

    def prepare_to_act(self):
        self.values = self.amplitude*np.sin(self.phase_offset + self.frequency*np.linspace(0, 2*np.pi, c.num_iterations))

    def set_value(self, robot, iteration):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex= robot.id,
                jointName= self.joint_name,
                controlMode= pblt.POSITION_CONTROL,
                targetPosition= self.values[iteration],
                maxForce= self.max_force
            )
    
    def save_values(self):
        with open("./data/{}_sensor_{}.npy".format(datetime.now().strftime('%Y%m%d_%H%M'), self.joint_name), 'wb') as f:
            np.save(f, self.values)
            f.close()
