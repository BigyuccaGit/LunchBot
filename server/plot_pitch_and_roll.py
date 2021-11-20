import vpython as vp
from robot_imu import RobotImu, ImuFusion
from delta_timer import DeltaTimer
import imu_settings

imu = RobotImu(gyro_offsets=imu_settings.gyro_offsets)
#imu = RobotImu()
fusion = ImuFusion(imu)

vp.graph(xmin=0, xmax=60, scroll=True)
graph_pitch = vp.gcurve(color=vp.color.red)
graph_roll = vp.gcurve(color=vp.color.green)

timer = DeltaTimer()
while True:
    vp.rate(100)
    dt, elapsed = timer.update()
    fusion.update(dt)
    pitch,roll = imu.read_accelerometer_pitch_and_roll()
    graph_pitch.plot(elapsed, fusion.pitch)
    graph_roll.plot(elapsed, fusion.roll)
#    graph_pitch.plot(elapsed, pitch)
#    graph_roll.plot(elapsed, roll)
