import world, robot
import pybullet as pblt
import pybullet_data
import constants as c
import time

class Simulation:

    def __init__(self):
        self.physics_client = pblt.connect(pblt.GUI)

        pblt.setAdditionalSearchPath(pybullet_data.getDataPath())

        pblt.setGravity(0, 0, -9.8)

        self.world = world.World()
        self.robot = robot.Robot()

    def run(self):
        for iteration in range(c.num_iterations):

            pblt.stepSimulation()
            self.robot.sense(iteration)
            self.robot.act(iteration)
            self.robot.think()
            time.sleep(c.sleep_time)

    def __del__(self):
        pblt.disconnect()
