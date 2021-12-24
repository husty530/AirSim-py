from pynput import keyboard as kb
import time, math, threading, airsim

class VirtualVehicle:

    def __init__(self):

        self.car = airsim.CarClient()
        self.car.confirmConnection()
        self.car.enableApiControl(True, 'Car')
        self.operation = self.car.getCarControls('Car')
        self.operation.is_manual_gear = True
        self.throttle = 0
        self.isOpened = True

    # キー入力で操作するやつ
    def operate(self, key):

        if key is kb.Key.esc:
            self.throttle = 0
            self.operation.steering = 0
            self.isOpened = False
        elif key is kb.Key.up:
            self.throttle += 0.2
        elif key is kb.Key.down:
            self.throttle -= 0.2
        elif key is kb.Key.left:
            self.operation.steering -= (2 * math.pi / 180)
        elif key is kb.Key.right:
            self.operation.steering += (2 * math.pi / 180)

        if self.throttle < 0:
            self.operation.manual_gear = -1
        else:
            self.operation.manual_gear = 1
        self.operation.throttle = abs(self.throttle)
        self.car.setCarControls(self.operation, 'Car')

    # 車載センサの情報をくれるやつ
    def getState(self):

        speed = self.car.getCarState('Car').speed
        imu = self.car.getImuData('Imu', 'Car').angular_velocity
        gps = self.car.getGpsData('Gps', 'Car').gnss.geo_point
        self.car.setCarControls(self.operation, 'Car')
        return {
            'speed': speed, 
            'latitude': gps.latitude, 
            'longitude': gps.longitude, 
            'gyro_x': imu.x_val, 
            'gyro_y': imu.y_val, 
            'gyro_z': imu.z_val
            }


if __name__ == '__main__':

    vehicle = VirtualVehicle()
    lock = threading.Lock()

    def receivingLoop():
        while vehicle.isOpened:
            with lock:
                print(vehicle.getState())
                time.sleep(0.1)
    
    def on_press(key):
        with lock:
            vehicle.operate(key)
    
    th1 = threading.Thread(target=receivingLoop)
    th2 = kb.Listener(on_press=on_press)
    th1.start()
    th2.start()
    th1.join()
    th2.join()