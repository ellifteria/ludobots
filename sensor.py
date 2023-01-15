import numpy as np
import pyrosim_modded.pyrosim_modded as pyrosim
from datetime import datetime

import constants as c

class Sensor:

    def __init__(self, link_name):
        self.link_name = link_name
        self.values = np.empty(c.num_iterations)

    def get_value(self, iteration):
        self.values[iteration] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.link_name)

    def save_values(self):
        with open("./data/{}_sensor_{}.npy".format(datetime.now().strftime('%Y%m%d_%H%M'), self.link_name), 'wb') as f:
            np.save(f, self.values)
            f.close()
