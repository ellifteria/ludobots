import pyrosim_modded.pyrosim_modded as pyrosim

def define_robot(body_size: int, leg_size: int):
    pyrosim.Send_Cube(
        name="torso",
        pos=[0, 0, body_size],
        size=[body_size,body_size, body_size])
    
    # create_front_left_leg(body_size, leg_size)
    # create_front_right_leg(body_size, leg_size)
    # create_back_left_leg(body_size, leg_size)
    # create_back_right_leg(body_size, leg_size)
    create_right_back_leg(body_size, leg_size)
    create_right_front_leg(body_size, leg_size)
    create_left_back_leg(body_size, leg_size)
    create_left_front_leg(body_size, leg_size)

def create_front_left_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_frontleftcoxa",
        parent="torso",
        child="frontleftcoxa",
        type="revolute",
        position=[-.4*body_size, 0.5*body_size, body_size],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="frontleftcoxa",
        pos=[0, 0.1*body_size, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="frontleftcoxa_frontleftfemur",
        parent="frontleftcoxa",
        child="frontleftfemur",
        type="revolute",
        position=[0, 0.2*body_size, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="frontleftfemur",
        pos=[0, 0.5*leg_size, 0],
        size=[.2*body_size, leg_size, .2*body_size])
    
    pyrosim.Send_Joint(
        name="frontleftfemur_frontlefttibia",
        parent="frontleftfemur",
        child="frontlefttibia",
        type="revolute",
        position=[0, leg_size, 0],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="frontlefttibia",
        pos=[0, 0, -0.5*body_size],
        size=[.2*body_size, .2*body_size, body_size])
    
def create_front_right_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_frontrightcoxa",
        parent="torso",
        child="frontrightcoxa",
        type="revolute",
        position=[.4*body_size, 0.5*body_size, body_size],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="frontrightcoxa",
        pos=[0, 0.1*body_size, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="frontrightcoxa_frontrightfemur",
        parent="frontrightcoxa",
        child="frontrightfemur",
        type="revolute",
        position=[0, 0.2*body_size, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="frontrightfemur",
        pos=[0, 0.5*leg_size, 0],
        size=[.2*body_size, leg_size, .2*body_size])
    
    pyrosim.Send_Joint(
        name="frontrightfemur_frontrighttibia",
        parent="frontrightfemur",
        child="frontrighttibia",
        type="revolute",
        position=[0, leg_size, 0],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="frontrighttibia",
        pos=[0, 0, -0.5*body_size],
        size=[.2*body_size, .2*body_size, body_size])
    
def create_back_left_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_backleftcoxa",
        parent="torso",
        child="backleftcoxa",
        type="revolute",
        position=[-.4*body_size, -0.5*body_size, body_size],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="backleftcoxa",
        pos=[0, -0.1*body_size, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="backleftcoxa_backleftfemur",
        parent="backleftcoxa",
        child="backleftfemur",
        type="revolute",
        position=[0, -0.2*body_size, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="backleftfemur",
        pos=[0, -0.5*leg_size, 0],
        size=[.2*body_size, leg_size, .2*body_size])
    
    pyrosim.Send_Joint(
        name="backleftfemur_backlefttibia",
        parent="backleftfemur",
        child="backlefttibia",
        type="revolute",
        position=[0, -leg_size, 0],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="backlefttibia",
        pos=[0, 0, -0.5*body_size],
        size=[.2*body_size, .2*body_size, body_size])
    
def create_back_right_leg(body_size: int, leg_size: int):

    pyrosim.Send_Joint(
        name="torso_backrightcoxa",
        parent="torso",
        child="backrightcoxa",
        type="revolute",
        position=[.4*body_size, -0.5*body_size, body_size],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="backrightcoxa",
        pos=[0, -0.1*body_size, 0],
        size=[.2*body_size, .2*body_size, .1*body_size])
    
    pyrosim.Send_Joint(
        name="backrightcoxa_backrightfemur",
        parent="backrightcoxa",
        child="backrightfemur",
        type="revolute",
        position=[0, -0.2*body_size, 0],
        axis=[0, 0, 1])
    
    pyrosim.Send_Cube(
        name="backrightfemur",
        pos=[0, -0.5*leg_size, 0],
        size=[.2*body_size, leg_size, .2*body_size])
    
    pyrosim.Send_Joint(
        name="backrightfemur_backrighttibia",
        parent="backrightfemur",
        child="backrighttibia",
        type="revolute",
        position=[0, -leg_size, 0],
        axis=[1, 0, 0])
    
    pyrosim.Send_Cube(
        name="backrighttibia",
        pos=[0, 0, -0.5*body_size],
        size=[.2*body_size, .2*body_size, body_size])

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
    
    pyrosim.Send_Joint(
        name="rightbackfemur_rightbacktibia",
        parent="rightbackfemur",
        child="rightbacktibia",
        type="revolute",
        position=[leg_size, 0, 0],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="rightbacktibia",
        pos=[0, 0, -0.5*body_size],
        size=[.4*body_size, .4*body_size, body_size])
    
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
    
    pyrosim.Send_Joint(
        name="rightfrontfemur_rightfronttibia",
        parent="rightfrontfemur",
        child="rightfronttibia",
        type="revolute",
        position=[leg_size, 0, 0],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="rightfronttibia",
        pos=[0, 0, -0.5*body_size],
        size=[.4*body_size, .4*body_size, body_size])
    
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
    
    pyrosim.Send_Joint(
        name="leftbackfemur_leftbacktibia",
        parent="leftbackfemur",
        child="leftbacktibia",
        type="revolute",
        position=[-leg_size, 0, 0],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="leftbacktibia",
        pos=[0, 0, -0.5*body_size],
        size=[.4*body_size, .4*body_size, body_size])
    
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
    
    pyrosim.Send_Joint(
        name="leftfrontfemur_leftfronttibia",
        parent="leftfrontfemur",
        child="leftfronttibia",
        type="revolute",
        position=[-leg_size, 0, 0],
        axis=[0, 1, 0])
    
    pyrosim.Send_Cube(
        name="leftfronttibia",
        pos=[0, 0, -0.5*body_size],
        size=[.4*body_size, .4*body_size, body_size])
    