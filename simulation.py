import world, robot
import pybullet as pblt
import pybullet_data
import constants as c
import time

class Simulation:

    def __init__(self, pybullet_method, solution_id):
        self.pblt_mthd = pybullet_method
        if self.pblt_mthd == "DIRECT":
            self.physics_client = pblt.connect(pblt.DIRECT)
        elif self.pblt_mthd == "GUI":
            self.physics_client = pblt.connect(pblt.GUI)
        else:
            raise ValueError("Valid pybullet connection method required")

        pblt.setAdditionalSearchPath(pybullet_data.getDataPath())

        pblt.setGravity(0, 0, -9.8)

        self.world = world.World()
        self.robot = robot.Robot(solution_id)

    def run(self):
        for iteration in range(c.num_iterations):

            pblt.stepSimulation()
            self.robot.sense(iteration)
            self.robot.act()
            self.robot.think()
            if self.pblt_mthd != "DIRECT":
                time.sleep(c.sleep_time)

    def get_fitness(self) -> None:
        self.robot.get_fitness()

    def __del__(self):
        pblt.disconnect()
