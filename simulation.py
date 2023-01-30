import world, robot
import pybullet as pblt
import pybullet_data
import constants as c
import time

class Simulation:

    def __init__(self, pybullet_method):
        if pybullet_method == "DIRECT":
            self.physics_client = pblt.connect(pblt.DIRECT)
        elif pybullet_method == "GUI":
            self.physics_client = pblt.connect(pblt.GUI)
        else:
            raise ValueError("Valid pybullet connection method required")

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

    def get_fitness(self) -> None:
        self.robot.get_fitness()

    def __del__(self):
        pblt.disconnect()
