import numpy as np

num_iterations = 1000

amplitudes = {'torso_frontleg': np.pi/4, 'torso_backleg': np.pi/4}
phase_offsets = {'torso_frontleg': 0, 'torso_backleg': np.pi/4}
frequencies = {'torso_frontleg': 5, 'torso_backleg': 10}

max_forces = {'torso_frontleg': 15, 'torso_backleg': 15}

sleep_time = 0.5/60
