import world, robot, sensor, motor
import pybullet as pblt
import pybullet_data
import pyrosim_modded.pyrosim_modded as pyrosim
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
        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex= self.robot.id,
        #         jointName= "torso_backleg",
        #         controlMode= pblt.POSITION_CONTROL,
        #         targetPosition= front_motor_vals[i],
        #         maxForce= 15
        #     )

        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex= robot_id,
        #         jointName= "torso_frontleg",
        #         controlMode= pblt.POSITION_CONTROL,
        #         targetPosition= back_motor_vals[i],
        #         maxForce= 15
        #     )

        #     pblt.stepSimulation()

        #     backleg_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
        #     frontleg_sensor_vals[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
        #     print(backleg_sensor_vals[i])
        #     print(frontleg_sensor_vals[i])
            
            pblt.stepSimulation()
            self.robot.sense(iteration)
            time.sleep(c.sleep_time)
            print(iteration)

        # with open("./data/backleg_sensor_vals.npy", 'wb') as f:
        #     np.save(f, backleg_sensor_vals)
        #     f.close()
        # with open("./data/frontleg_sensor_vals.npy", 'wb') as f:
        #     np.save(f, frontleg_sensor_vals)
        #     f.close()

    def __del__(self):
        pblt.disconnect()
