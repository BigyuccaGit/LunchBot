import vpython as vp
from robot_imu import RobotImu
from imu_settings import mag_offsets
from statistics import median

#imu = RobotImu(mag_offsets=mag_offsets)
imu=RobotImu()

mag_min = vp.vector(0, 0, 0)
mag_max = vp.vector(0, 0, 0)

scatter_xy = vp.gdots(color=vp.color.red)
scatter_yz = vp.gdots(color=vp.color.green)
scatter_zx = vp.gdots(color=vp.color.blue)

total=vp.vector(0,0,0)

listx=[]
listy=[]
listz=[]

n=0
while True:
    vp.rate(100)
    n=n+1
    mag = imu.read_magnetometer()

    mag_min.x = min(mag_min.x, mag.x)
    mag_min.y = min(mag_min.y, mag.y)
    mag_min.z = min(mag_min.z, mag.z)

    mag_max.x = max(mag_max.x, mag.x)
    mag_max.y = max(mag_max.y, mag.y)
    mag_max.z = max(mag_max.z, mag.z)
    offset = (mag_max + mag_min) / 2

    total += mag

    listx.append(mag.x)
    listy.append(mag.y)
    listz.append(mag.z)

    medianx=median(listx)
    mediany=median(listy)
    medianz=median(listz)

    print(f"Magnetometer: {mag}. Offsets: {offset}.")
    print(f"Magnetometer: {mag}. Means: {total/n}.")
    print(f"Magnetometer: {mag}. Medians: {vp.vector(medianx, mediany, medianz)}.")
    
    scatter_xy.plot(mag.x, mag.y)
    scatter_yz.plot(mag.y, mag.z)
    scatter_zx.plot(mag.z, mag.x)
