import numpy as np
import pyrosim_modded.pyrosim_modded as pyrosim

import constants as c

class Sensor:

    def __init__(self, link_name):
        self.link_name = link_name
        self.values = np.empty(c.num_iterations)

    def get_value(self, iteration):
        curr_val = pyrosim.Get_Touch_Sensor_Value_For_Link(self.link_name)
        self.values[iteration] = curr_val
        if iteration >= c.num_iterations - 1:
            print(self.values)