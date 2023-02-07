import random
import pyrosim_modded.pyrosim_modded as pyrosim


def generate_terrain():
    num_blocks = 25
    block_area = [
        [-20, -20], # lowest (x, y)
        [20, 20]    # highest (x, y)
    ]
    block_sizes_range = [
        [1, 3],   # x
        [1, 3],   # y
        [0.5, 1]  # z
    ]

    pyrosim.Start_SDF("terrain.sdf")

    for i in range(num_blocks):
        size_x = random_in_range(block_sizes_range[0][0], block_sizes_range[0][1])
        size_y = random_in_range(block_sizes_range[1][0], block_sizes_range[1][1])
        size_z = random_in_range(block_sizes_range[2][0], block_sizes_range[2][1])
        pos_x = random_in_range(block_area[0][0], block_area[1][0])
        pos_y = random_in_range(block_area[0][1], block_area[1][1])
        pos_z = size_z / 2

        pyrosim.Send_Cube(name="box", pos=[pos_x, pos_y, pos_z, 'static'], size=[size_x, size_y, size_z])
    
    pyrosim.End()
        

def random_in_range(lower, upper):
    return (upper - lower) * random.random() + lower

generate_terrain()