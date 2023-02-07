import numpy as np

num_iterations = 2500*4

amplitudes = {'torso_frontleg': np.pi/4, 'torso_backleg': np.pi/4}
phase_offsets = {'torso_frontleg': 0, 'torso_backleg': 0}

frequencies = {'torso_frontleg': 5, 'torso_backleg': 10}

max_forces = {'torso_frontleg': 25, 'torso_backleg': 25}

sleep_time = 0

num_generations = 15

# population_size = 10

num_sensor_neurons = 9

num_motor_neurons = 5

motorJointRange = .2

default_fitness = 100


mutation_rate = 0.75
mutation_magnitude = 2

generation_size = 12
number_of_children = 5
family_filter_size = 3
random_members = 3

CPG_magnitude = 2
CPG_period_modifier = 2*np.pi