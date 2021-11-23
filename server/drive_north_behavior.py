"""This behavior will turn to seek north, and then drive that way"""
from robot_imu import RobotImu, ImuFusion
from delta_timer import DeltaTimer
from pid_controller import PIController
from robot import Robot
import imu_settings

# Set up the IMU
imu = RobotImu(mag_offsets=imu_settings.mag_offsets,
               gyro_offsets=imu_settings.gyro_offsets)

# Set up the sensor fusion algorithm
fusion = ImuFusion(imu)

# Set up the delta time calculation
timer = DeltaTimer()

# Set up the Proportional Integral (PI) controller
pid = PIController(0.7, 0.01)

# Set up the robot
robot = Robot()

# Set base spped
base_speed = 70

# Let's head for this heading
heading_set_point = 0

while True:
    # Get the delta time
    dt, elapsed = timer.update()
    
    # Get next set of (fused) readings
    fusion.update(dt)
    
    # Note error in heading
    heading_error = fusion.yaw - heading_set_point
    
    # Calculate steering correction using PIC
    steer_value = pid.get_value(heading_error, delta_time=dt)
    print(f"Error: {heading_error}, Value:{steer_value:2f}, t: {elapsed}")
    
    # Perform steering correction
    robot.set_left(base_speed + steer_value)
    robot.set_right(base_speed - steer_value)
