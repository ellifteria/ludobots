import numpy as np
import pybullet as pblt
from sensor import Sensor
from motor import Motor
import pyrosim_modded.pyrosim_modded as pyrosim
from pyrosim_modded.neuralNetwork import NEURAL_NETWORK
import time
import constants as Cnsts

import os

class Robot:

    def __init__(self, solution_id):
        self.id = pblt.loadURDF("./data/robot/body{}.urdf".format(solution_id))

        self.solution_id = solution_id

        pyrosim.Prepare_To_Simulate(self.id)

        self.prepare_to_sense()
        self.prepare_to_act()
        self.prepare_to_think()

        os.system("rm ./data/robot/brain{}.nndf".format(self.solution_id))
        os.system("rm ./data/robot/body{}.urdf".format(self.solution_id))

    def prepare_to_sense(self):
        self.sensors = {}
        for link_name in pyrosim.linkNamesToIndices:
            self.sensors[link_name] = Sensor(link_name)

    def prepare_to_act(self):
        self.motors = {}
        for joint_name in pyrosim.jointNamesToIndices:
            self.motors[joint_name] = Motor(joint_name)

    def prepare_to_think(self):
        self.nn = NEURAL_NETWORK("./data/robot/brain{}.nndf".format(self.solution_id))

    def sense(self, iteration):
        for sensor_name in self.sensors:
            self.sensors[sensor_name].get_value(iteration)
        torso_index = max([int(x[1:]) for x in self.nn.Get_Neuron_Names() if 's' in x])
        self.nn.neurons['s{}'.format(torso_index)].Set_Value(Cnsts.CPG_magnitude * np.sin(Cnsts.CPG_period_modifier * iteration))

    def act(self):
        for neuron_name in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuron_name):
                joint_name = self.nn.Get_Motor_Neuron_Joint(neuron_name)
                desired_angle = self.nn.Get_Value_Of(neuron_name)
                self.motors[joint_name].set_value(self, desired_angle)

    def think(self):
        self.nn.Update()

    def save_sensor_motor_data(self):
        for sensor_name in self.sensors:
            self.sensors[sensor_name].save_values()
        for motor_name in self.motors:
            self.motors[motor_name].save_values()

    def get_fitness(self) -> None:
        base_pos_orientation = pblt.getBasePositionAndOrientation(self.id)
        base_pos = base_pos_orientation[0]
        link_0_x = base_pos[0]
        link_0_y = base_pos[1]
        link_0_z = base_pos[2]
        self.save_fitness(link_0_y)

    def save_fitness(self, fitness) -> None:
        time.sleep(0.02)
        with open("./data/robot/tmp_fitness{}.txt".format(self.solution_id), 'w') as f:
            f.write(str(fitness))
            time.sleep(0.02)
            f.close()
        os.system("mv ./data/robot/tmp_fitness{}.txt ./data/robot/robot_fitness{}.txt".format(self.solution_id, self.solution_id))

