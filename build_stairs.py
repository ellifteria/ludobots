import random
import pyrosim_modded.pyrosim_modded as pyrosim


def generate_terrain():
    size_x = 1.25
    size_y = 20
    init_size_z = 0.15
    init_pos_x = -1.9-size_x/2
    pos_y = 0
    init_pos_z = init_size_z/2

    pyrosim.Start_SDF("terrain.sdf")
    
    num_steps = 10

    for step in range(num_steps):
        pos_x = init_pos_x - step * size_x
        size_z = init_size_z + step * 2 * init_size_z
        pos_z = init_pos_z + step * init_size_z
        pyrosim.Send_Cube(name="box", pos=[pos_x, pos_y, pos_z, 'static'], size=[size_x, size_y, size_z])
    
    pyrosim.End()
        

def random_in_range(lower, upper):
    return (upper - lower) * random.random() + lower

generate_terrain()