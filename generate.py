import pyrosim.pyrosim as pyrosim

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

    pyrosim.Send_Joint(name="torso_frontleg", parent="torso", child="frontleg", type="revolute", position=[0, -0.5, 1])

    pyrosim.Send_Cube(name="frontleg", pos=[0, -0.5, -0.5], size=[l, w, h])

    pyrosim.Send_Joint(name="torso_backleg", parent="torso", child="backleg", type="revolute", position=[0, 0.5, 1])

    pyrosim.Send_Cube(name="backleg", pos=[0, 0.5, -0.5], size=[l, w, h])

    pyrosim.End()


def main():
    create_world()
    create_robot()

if __name__=="__main__":
    main()