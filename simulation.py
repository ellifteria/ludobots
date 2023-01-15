import world, robot, sensor, motor

class Simulation:

    def __init__(self):
        self.world = world.World()
        self.robot = robot.Robot()
        self.sensors = {}
        self.motors = {}