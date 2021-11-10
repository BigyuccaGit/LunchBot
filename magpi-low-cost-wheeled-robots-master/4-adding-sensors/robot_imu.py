from icm20948 import ICM20948
from vpython import vector


class RobotImu:
    """Define a common interface to an inertial measurement unit with temperature"""
    # NOTE: y and z axes negated to reflect actual orientation of ICM20948
    def __init__(self, gyro_offsets = None ):
        self._imu = ICM20948()
        self.gyro_offsets = gyro_offsets or vector(0,0,0)

    def read_temperature(self):
        """Read a temperature in degrees C."""
        return self._imu.read_temperature()

    def read_gyroscope(self):
        """Return prescaled gyro data"""
        _, _, _, x, y, z = self._imu.read_accelerometer_gyro_data()
 #       return vector(x, y, z)
        return vector(x, -y, -z) - self.gyro_offsets

    def read_accelerometer(self):
        """Return accelerometer data"""
        accel_x, accel_y, accel_z, _, _, _ = self._imu.read_accelerometer_gyro_data()
 #       return vector(accel_x, accel_y, accel_z)
        return vector(accel_x, -accel_y, -accel_z)

    def read_magnetometer(self):
        """Return magnetometer data"""
        mag_x, mag_y, mag_z = self._imu.read_magnetometer_data()
#        return vector(mag_x, -mag_y, -mag_z)
        return vector(mag_x, mag_y, mag_z)

