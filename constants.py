import numpy as np

num_iterations = 10000

amplitudes = {'torso_frontleg': np.pi/4, 'torso_backleg': np.pi/4}
phase_offsets = {'torso_frontleg': 0, 'torso_backleg': 0}

frequencies = {'torso_frontleg': 5, 'torso_backleg': 10}

max_forces = {'torso_frontleg': 25, 'torso_backleg': 25}

sleep_time = 0.0001/6000

num_generations = 10
