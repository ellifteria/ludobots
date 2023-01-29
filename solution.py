import numpy as np
import pyrosim_modded.pyrosim_modded as pyrosim
import os

class Solution:
    
    def __init__(self, network_shape = [3,2]) -> None:
        self.weights = -1+2*np.random.rand(*network_shape)

    def evaluate(self) -> None:
        self.create_world()
        self.generate_body()
        self.generate_brain()
        os.system("python simulate.py")

    def create_world(self) -> None:
        l = 1
        w = 1
        h = 1

        x = -2
        y = 2
        z = h/2

        pyrosim.Start_SDF("box.sdf")

        pyrosim.Send_Cube(name="box", pos=[x, y, z], size=[l, w, h])

        pyrosim.End()

    def generate_body(self) -> None:
        l = 1
        w = 1
        h = 1

        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="torso", pos=[0, 0, 1.5], size=[l, w, h])

        pyrosim.Send_Joint(name="torso_frontleg", parent="torso", child="frontleg", type="revolute", position=[-0.5, 0, 1], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="frontleg", pos=[-0.5, 0, -0.5], size=[l, w, h])

        pyrosim.Send_Joint(name="torso_backleg", parent="torso", child="backleg", type="revolute", position=[0.5, 0, 1], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="backleg", pos=[0.5, 0, -0.5], size=[l, w, h])

        pyrosim.End()

    def generate_brain(self) -> None:
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name= '0', linkName="torso")
        pyrosim.Send_Sensor_Neuron(name= '1', linkName="backleg")
        pyrosim.Send_Sensor_Neuron(name= '2', linkName="frontleg")
        pyrosim.Send_Motor_Neuron(name= '3', jointName='torso_backleg')
        pyrosim.Send_Motor_Neuron(name= '4', jointName='torso_frontleg')

        num_sensor_neurons = 2
        num_motor_neurons = 3
        first_motor_neurons = 3

        for row in range(num_motor_neurons):
            for col in range(num_sensor_neurons):
                pyrosim.Send_Synapse(
                    sourceNeuronName=str(row),
                    targetNeuronName=str(first_motor_neurons+col),
                    weight=self.weights[row, col]
                )

        pyrosim.End()    
