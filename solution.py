import numpy as np
import pyrosim_modded.pyrosim_modded as pyrosim
import define_robot
import os
import time
import constants as Cnsts
import warnings

class Solution:
    
    def __init__(self, solution_id = 0, genome = None) -> None:
        self.dirs_axis_1 = ['front', 'back']
        self.dirs_axis_2 = ['left', 'right']

        self.body_parts = ['torso', '{}{}coxa', '{}{}femur']

        num_sensor_neurons =  (len(self.dirs_axis_1) + len(self.dirs_axis_2)) + 1
        num_motor_neurons = (len(self.body_parts) - 1)  * (len(self.dirs_axis_1) + len(self.dirs_axis_2))
        self.network_shape = [num_sensor_neurons, num_motor_neurons]
        self.solution_id = solution_id
        if genome is None:
            self.weights = -5+10*np.random.rand(*self.network_shape)
        else:
            self.weights = genome

        self.mutation_rate = Cnsts.mutation_rate
        self.mutation_magnitude = Cnsts.mutation_magnitude

    def start_simulation(self, pybullet_method = "DIRECT") -> None:
        self.generate_body()
        self.generate_brain()
        os.system("python simulate.py {} {} &".format(pybullet_method, self.solution_id))

    def wait_for_simulation_to_end(self) -> None:
        time.sleep(0.02)
        fitness_file_name = "./data/robot/robot_fitness{}.txt".format(self.solution_id)
        timeout = time.time() + 60 * 10
        while not os.path.exists(fitness_file_name):
            time.sleep(0.02)
            if time.time() > timeout:
                warnings.warn("Warning: simulation timed out")
                os.system("rm {}".format(fitness_file_name))
                self.fitness = Cnsts.default_fitness
                return
        with open(fitness_file_name, 'r') as f:
            fitness = f.read()
            self.fitness = float(fitness)
            f.close()
        time.sleep(0.02)
        os.system("rm {}".format(fitness_file_name))

    def mutate(self) -> None:
        if np.random.rand() < self.mutation_rate:
            row_to_mutate = np.random.randint(1, self.weights.shape[0])
            col_to_mutate = np.random.randint(1, self.weights.shape[1])
            new_neuron_value = self.mutation_magnitude * (-0.5 + np.random.rand())
            self.weights[row_to_mutate, col_to_mutate] = new_neuron_value

    def generate_body(self) -> None:
        pyrosim.Start_URDF("./data/robot/body{}.urdf".format(self.solution_id))
        define_robot.define_robot(body_size=1, leg_size=1)
        pyrosim.End()

    def generate_brain(self) -> None:
        pyrosim.Start_NeuralNetwork("./data/robot/brain{}.nndf".format(self.solution_id))

        sensor_neuron_index = 0
        motor_neuron_index = 0

        motor_neurons = {}
        sensor_neurons = {}

        for dir1 in self.dirs_axis_1:
            for dir2 in self.dirs_axis_2:
                sensor_neuron = '{}{}femur'.format(dir2, dir1)

                sensor_neurons[sensor_neuron] = sensor_neuron_index
                sensor_neuron_index += 1

                for index in range(len(self.body_parts) - 1):
                    motor_neuron = '' + self.body_parts[index].format(dir2, dir1) + '_' + self.body_parts[index + 1].format(dir2, dir1)
                    
                    motor_neurons[motor_neuron] = motor_neuron_index
                    motor_neuron_index += 1

        sensor_neurons['torso'] = sensor_neuron_index

        for sensor_neuron in sensor_neurons:
            pyrosim.Send_Sensor_Neuron(name= "s" + str(sensor_neurons[sensor_neuron]), linkName=sensor_neuron)

        for motor_neuron in motor_neurons:
            pyrosim.Send_Motor_Neuron(name= "m" + str(motor_neurons[motor_neuron]), jointName=motor_neuron)


        for sensor_neuron in sensor_neurons:
            for motor_neuron in motor_neurons:
                sensor_neurons_number = sensor_neurons[sensor_neuron]
                motor_neurons_number = motor_neurons[motor_neuron]
                pyrosim.Send_Synapse(
                    sourceNeuronName="s" + str(sensor_neurons_number),
                    targetNeuronName="m" + str(motor_neurons_number),
                    weight=self.weights[sensor_neurons_number, motor_neurons_number]
                )

        pyrosim.End()
