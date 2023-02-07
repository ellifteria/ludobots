import pybullet as pblt

class World:

    def __init__(self):
        self.plane_id = pblt.loadURDF("plane.urdf")

        # pblt.loadSDF("./data/world/terrain.sdf")

        # terrainShape = p.createCollisionShape(shapeType = p.GEOM_HEIGHTFIELD, meshScale=[.5,.5, 0.2],fileName = "heightmaps/ground0.txt", heightfieldTextureScaling=128)
        # terrain  = p.createMultiBody(0, terrainShape)
        # p.resetBasePositionAndOrientation(terrain,[0,0,0], [0,0,0,1])