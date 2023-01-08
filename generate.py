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

    pyrosim.Send_Cube(name="link0", pos=[0, 0, 0.5], size=[l, w, h])

    pyrosim.Send_Joint(name="link0_link1", parent="link0", child="link1", type="revolute", position=[0, 0, 1])

    pyrosim.Send_Cube(name="link1", pos=[0, 0, 0.5], size=[l, w, h])

    pyrosim.Send_Joint(name="link1_link2", parent="link1", child="link2", type="revolute", position=[0, 0, 1])

    pyrosim.Send_Cube(name="link2", pos=[0, 0, 0.5], size=[l, w, h])

    pyrosim.Send_Joint(name="link2_link3", parent="link2", child="link3", type="revolute", position=[0, 0.5, 0.5])

    pyrosim.Send_Cube(name="link3", pos=[0, 0.5, 0], size=[l, w, h])

    pyrosim.Send_Joint(name="link3_link4", parent="link3", child="link4", type="revolute", position=[0, 1, 0])

    pyrosim.Send_Cube(name="link4", pos=[0, 0.5, 0], size=[l, w, h])

    pyrosim.Send_Joint(name="link4_link5", parent="link4", child="link5", type="revolute", position=[0, 0.5, -0.5])

    pyrosim.Send_Cube(name="link5", pos=[0, 0, -0.5], size=[l, w, h])

    pyrosim.Send_Joint(name="link5_link6", parent="link5", child="link6", type="revolute", position=[0, 0, -1])

    pyrosim.Send_Cube(name="link6", pos=[0, 0, -0.5], size=[l, w, h])

    pyrosim.End()


def main():
    create_world()
    create_robot()

if __name__=="__main__":
    main()