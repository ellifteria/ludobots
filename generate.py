import pyrosim_modded.pyrosim_modded as pyrosim

import fileinput

def replace_txt(filename, txt_to_replace, new_txt):

    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(txt_to_replace, new_txt), end='')

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

def create_robot():
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

    # replace_txt("body.urdf", '<axis xyz="0 1 0"/>', '<axis xyz="1 0 0"/>')


def main():
    create_world()
    create_robot()

if __name__=="__main__":
    main()