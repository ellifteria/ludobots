import numpy as np
import matplotlib.pyplot as plt

with open("./data/backleg_sensor_vals.npy", 'rb') as f:
    backleg_sensor_vals = np.load(f)
    f.close()

with open("./data/frontleg_sensor_vals.npy", 'rb') as f:
    frontleg_sensor_vals = np.load(f)
    f.close()

with open("./data/backleg_motor_vals.npy", 'rb') as f:
    backleg_motor_vals = np.load(f)
    f.close()

with open("./data/frontleg_motor_vals.npy", 'rb') as f:
    frontleg_motor_vals = np.load(f)
    f.close()

plt.plot(backleg_sensor_vals, '-', label="Back leg touch sensor", linewidth=2)
plt.plot(frontleg_sensor_vals, '-', label="Front leg touch sensor", linewidth=1.5)
plt.legend()
plt.show()

plt.plot(backleg_motor_vals, '-', label="Back leg motor", linewidth=2)
plt.plot(frontleg_motor_vals, '-', label="Front leg motor", linewidth=1)
plt.legend()
plt.show()