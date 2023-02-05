import numpy as np
import pyrosim_modded.pyrosim_modded as pyrosim
import os
import time
import constants as Cnsts

class Solution:
    
    def __init__(self, solution_id = 0) -> None:
        self.network_shape = [Cnsts.num_sensor_neurons, Cnsts.num_motor_neurons]
        self.solution_id = solution_id
        self.weights = -1+2*np.random.rand(*self.network_shape)

    def start_simulation(self, pybullet_method = "DIRECT") -> None:
        self.create_world()
        self.generate_body()
        self.generate_brain()
        os.system("python simulate.py {} {} &".format(pybullet_method, self.solution_id))

    def wait_for_simulation_to_end(self) -> None:
        time.sleep(0.02)
        fitness_file_name = "./data/robot/robot_fitness{}.txt".format(self.solution_id)
        while not os.path.exists(fitness_file_name):
            time.sleep(0.02)
        with open(fitness_file_name, 'r') as f:
            fitness = f.read()
            self.fitness = float(fitness)
            f.close()
        time.sleep(0.02)
        os.system("rm {}".format(fitness_file_name))

    def mutate(self) -> None:
        row_to_mutate = np.random.randint(1, self.weights.shape[0])
        col_to_mutate = np.random.randint(1, self.weights.shape[1])
        new_neuron_value = -1+2*np.random.rand()
        self.weights[row_to_mutate, col_to_mutate] = new_neuron_value

    def create_world(self) -> None:
        l = 1
        w = 1
        h = 1

        x = -2
        y = 2
        z = h/2

        pyrosim.Start_SDF("./data/world/box.sdf")

        pyrosim.Send_Cube(name="box", pos=[x, y, z], size=[l, w, h])

        pyrosim.End()

    def generate_body(self) -> None:
        l = 1
        w = 1
        h = 1

        pyrosim.Start_URDF("./data/robot/body.urdf")

        pyrosim.Send_Cube(name="torso", pos=[0, 0, 1], size=[l, w, h])

        pyrosim.Send_Joint(name="torso_frontleg", parent="torso", child="frontleg", type="revolute", position=[0, 0.5, 1], axis=[1, 0, 0])

        pyrosim.Send_Cube(name="frontleg", pos=[0, 0.5, 0], size=[.2, 1, .2])

        pyrosim.Send_Joint(name="torso_backleg", parent="torso", child="backleg", type="revolute", position=[0, -0.5, 1], axis=[1, 0, 0])

        pyrosim.Send_Cube(name="backleg", pos=[0, -.5, 0], size=[.2, 1, .2])

        pyrosim.Send_Joint(name="torso_leftleg", parent="torso", child="leftleg", type="revolute", position=[-0.5, 0, 1], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="leftleg", pos=[-.5, 0, 0], size=[1, .2, .2])

        pyrosim.Send_Joint(name="torso_rightleg", parent="torso", child="rightleg", type="revolute", position=[0.5, 0, 1], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="rightleg", pos=[.5, 0, 0], size=[1, .2, .2])

        pyrosim.Send_Joint(name="frontleg_frontleglower", parent="frontleg", child="frontleglower", type="revolute", position=[0, 1, 0], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="frontleglower", pos=[0, 0, -.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="backleg_backleglower", parent="backleg", child="backleglower", type="revolute", position=[0, -1, 0], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="backleglower", pos=[0, 0, -.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="rightleg_rightleglower", parent="rightleg", child="rightleglower", type="revolute", position=[1, 0, 0], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="rightleglower", pos=[0, 0, -.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="leftleg_leftleglower", parent="leftleg", child="leftleglower", type="revolute", position=[-1, 0, 0], axis=[0, 1, 0])

        pyrosim.Send_Cube(name="leftleglower", pos=[0, 0, -.5], size=[.2, .2, 1])

        pyrosim.End()

    def generate_brain(self) -> None:
        pyrosim.Start_NeuralNetwork("./data/robot/brain{}.nndf".format(self.solution_id))
        pyrosim.Send_Sensor_Neuron(name= '0', linkName="torso")
        pyrosim.Send_Sensor_Neuron(name= '1', linkName="backleglower")
        pyrosim.Send_Sensor_Neuron(name= '2', linkName="frontleglower")
        pyrosim.Send_Sensor_Neuron(name= '3', linkName="rightleglower")
        pyrosim.Send_Sensor_Neuron(name= '4', linkName="leftleglower")
        pyrosim.Send_Motor_Neuron(name= '5', jointName='torso_backleg')
        pyrosim.Send_Motor_Neuron(name= '6', jointName='torso_frontleg')
        pyrosim.Send_Motor_Neuron(name= '7', jointName='torso_rightleg')
        pyrosim.Send_Motor_Neuron(name= '8', jointName='torso_leftleg')
        pyrosim.Send_Motor_Neuron(name= '9', jointName='backleg_backleglower')
        pyrosim.Send_Motor_Neuron(name= '10', jointName='frontleg_frontleglower')
        pyrosim.Send_Motor_Neuron(name= '11', jointName='rightleg_rightleglower')
        pyrosim.Send_Motor_Neuron(name= '12', jointName='leftleg_leftleglower')

        num_sensor_neurons = self.network_shape[0]
        num_motor_neurons = self.network_shape[1]
        first_motor_neurons = num_sensor_neurons + 1

        for row in range(num_sensor_neurons):
            for col in range(num_motor_neurons):
                pyrosim.Send_Synapse(
                    sourceNeuronName=str(row),
                    targetNeuronName=str(first_motor_neurons+col),
                    weight=self.weights[row, col]
                )

        pyrosim.End()    
