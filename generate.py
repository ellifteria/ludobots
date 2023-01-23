import pyrosim_modded.pyrosim_modded as pyrosim
import random

def create_world():
    l = 1
    w = 1
    h = 1

    x = -2
    y = 2
    z = h/2

    pyrosim.Start_SDF("box.sdf")

    pyrosim.Send_Cube(name="box", pos=[x, y, z], size=[l, w, h])

    pyrosim.End()

def generate_body():
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

def generate_brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name= '0', linkName="torso")
    pyrosim.Send_Sensor_Neuron(name= '1', linkName="backleg")
    pyrosim.Send_Sensor_Neuron(name= '2', linkName="frontleg")
    pyrosim.Send_Motor_Neuron(name= '3', jointName='torso_backleg')
    pyrosim.Send_Motor_Neuron(name= '4', jointName='torso_frontleg')

    sensor_neurons = (0,2)
    motor_neurons = (3,4)

    for i in range(sensor_neurons[0], sensor_neurons[1]+1):
        for j in range(motor_neurons[0], motor_neurons[1]+1):
            pyrosim.Send_Synapse(
                sourceNeuronName=str(i),
                targetNeuronName=str(j),
                weight=2*random.random()-1
            )

    pyrosim.End()    

def create_robot():
    generate_body()
    generate_brain()

def main():
    create_world()
    create_robot()

if __name__=="__main__":
    main()