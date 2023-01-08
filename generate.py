import pyrosim.pyrosim as pyrosim

base_l = 1
base_w = 1
base_h = 1

base_x = 0
base_y = 0
base_z = base_h/2

base_name = "box_{}_{}_{}"

pyrosim.Start_SDF("tower_boxes.sdf")

for box_x in range(5):
    for box_y in range(5):
        for box_z in range(10):
            l = base_l * .9 ** (box_z)
            w = base_w * .9 ** (box_z)
            h = base_h * .9 ** (box_z)
            x = base_x + box_x * base_l
            y = base_y + box_y * base_w
            z = base_z + box_z * base_h
            box_name = base_name.format(box_x, box_y, box_z)
            pyrosim.Send_Cube(name=box_name, pos=[x, y, z], size=[l, w, h])

pyrosim.End()