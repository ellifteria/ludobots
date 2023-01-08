import pyrosim.pyrosim as pyrosim

l = 1
w = 1
h = 1

x = 0
y = 0
z = h/2

pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="box", pos=[x, y, z], size=[l, w, h])

pyrosim.End()