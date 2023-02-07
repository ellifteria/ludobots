dirs_axis_1 = ['front', 'back']
dirs_axis_2 = ['left', 'right']

body_parts = ['torso', '{}{}coxa', '{}{}femur', '{}{}tibia']

motor_neuron_index = 0
sensor_neuron_index = 0

motor_neurons = {}
sensor_neurons = {}

for dir1 in dirs_axis_1:
    for dir2 in dirs_axis_2:
        for index in range(len(body_parts) - 1):
            motor_neuron1 = '' + body_parts[index].format(dir1, dir2) + '_' + body_parts[index + 1].format(dir1, dir2)
            motor_neuron2 = '' + body_parts[index].format(dir2, dir1) + '_' + body_parts[index + 1].format(dir2, dir1)
            motor_neurons[motor_neuron1] = motor_neuron_index
            motor_neuron_index += 1
            motor_neurons[motor_neuron2] = motor_neuron_index
            motor_neuron_index += 1
            sensor_neuron1 = '' + body_parts[index + 1].format(dir1, dir2)
            sensor_neuron2 = '' + body_parts[index + 1].format(dir2, dir1)
            sensor_neurons[sensor_neuron1] = sensor_neuron_index
            sensor_neuron_index += 1
            sensor_neurons[sensor_neuron2] = sensor_neuron_index
            sensor_neuron_index += 1

print(motor_neurons)
print(sensor_neurons)
