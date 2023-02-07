import pybullet as pblt

class World:

    def __init__(self):
        self.plane_id = pblt.loadURDF("plane.urdf")