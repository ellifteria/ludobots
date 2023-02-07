import pyrosim_modded.pyrosim_modded as pyrosim

def define_robot(body_size: int, leg_size: int):
    pyrosim.Send_Cube(
        name="torso",
        pos=[0, 0, body_size],
        size=[body_size,body_size, 0.5*body_size])
    
    create_right_back_leg(body_size, 2*leg_size)
    create_right_front_leg(body_size, 2*leg_size)
    create_left_back_leg(body_size, 2*leg_size)
    create_left_front_leg(body_size, 2*leg_size)

def create_right_back_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_rightbackcoxa",
        parent="torso",
        child="rightbackcoxa",
        type="revolute",
        position=[0.5*body_size, -.4*body_size, body_size],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="rightbackcoxa",
        pos=[0.1*body_size, 0, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="rightbackcoxa_rightbackfemur",
        parent="rightbackcoxa",
        child="rightbackfemur",
        type="revolute",
        position=[0.2*body_size, 0, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="rightbackfemur",
        pos=[0.5*leg_size, 0, 0],
        size=[leg_size, .2*body_size, .2*body_size])
    
    # pyrosim.Send_Joint(
    #     name="rightbackfemur_rightbacktibia",
    #     parent="rightbackfemur",
    #     child="rightbacktibia",
    #     type="revolute",
    #     position=[leg_size, 0, 0],
    #     axis=[0, 1, 0])
    
    # pyrosim.Send_Cube(
    #     name="rightbacktibia",
    #     pos=[0, 0, -0.5*body_size],
    #     size=[.4*body_size, .4*body_size, body_size])
    
def create_right_front_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_rightfrontcoxa",
        parent="torso",
        child="rightfrontcoxa",
        type="revolute",
        position=[0.5*body_size, .4*body_size, body_size],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="rightfrontcoxa",
        pos=[0.1*body_size, 0, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="rightfrontcoxa_rightfrontfemur",
        parent="rightfrontcoxa",
        child="rightfrontfemur",
        type="revolute",
        position=[0.2*body_size, 0, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="rightfrontfemur",
        pos=[0.5*leg_size, 0, 0],
        size=[leg_size, .2*body_size, .2*body_size])
    
def create_left_back_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_leftbackcoxa",
        parent="torso",
        child="leftbackcoxa",
        type="revolute",
        position=[-0.5*body_size, -.4*body_size, body_size],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="leftbackcoxa",
        pos=[-0.1*body_size, 0, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="leftbackcoxa_leftbackfemur",
        parent="leftbackcoxa",
        child="leftbackfemur",
        type="revolute",
        position=[-0.2*body_size, 0, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="leftbackfemur",
        pos=[-0.5*leg_size, 0, 0],
        size=[leg_size, .2*body_size, .2*body_size])
    
def create_left_front_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_leftfrontcoxa",
        parent="torso",
        child="leftfrontcoxa",
        type="revolute",
        position=[-0.5*body_size, .4*body_size, body_size],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="leftfrontcoxa",
        pos=[-0.1*body_size, 0, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="leftfrontcoxa_leftfrontfemur",
        parent="leftfrontcoxa",
        child="leftfrontfemur",
        type="revolute",
        position=[-0.2*body_size, 0, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="leftfrontfemur",
        pos=[-0.5*leg_size, 0, 0],
        size=[leg_size, .2*body_size, .2*body_size])
