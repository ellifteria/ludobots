import pybullet as pblt
from sensor import Sensor
from motor import Motor
import pyrosim_modded.pyrosim_modded as pyrosim
from pyrosim_modded.neuralNetwork import NEURAL_NETWORK

class Robot:

    def __init__(self):
        self.id = pblt.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.id)

        self.prepare_to_sense()
        self.prepare_to_act()
        self.prepare_to_think()

    def prepare_to_sense(self):
        self.sensors = {}
        for link_name in pyrosim.linkNamesToIndices:
            self.sensors[link_name] = Sensor(link_name)

    def prepare_to_act(self):
        self.motors = {}
        for joint_name in pyrosim.jointNamesToIndices:
            self.motors[joint_name] = Motor(joint_name)

    def prepare_to_think(self):
        self.nn = NEURAL_NETWORK("brain.nndf")

    def sense(self, iteration):
        for sensor in self.sensors:
            self.sensors[sensor].get_value(iteration)

    def act(self, iteration):
        for motor in self.motors:
            self.motors[motor].set_value(self, iteration)

    def think(self):
        self.nn.Update()
        self.nn.Print()

    def save_data(self):
        for sensor in self.sensors:
            self.sensors[sensor].save_values()
        for motor in self.motors:
            self.motors[motor].save_values()

