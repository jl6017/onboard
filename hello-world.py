import sys
from math import sin, cos
from pylx16a.lx16a import *
import time
import numpy as np

LX16A.initialize("/dev/cu.usbserial-2130", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
start_angle = 40
up_angle = 30
init_angles = [30, 225 + 5, 230, 40, 30 - 10, 205]
step_len = 3
while True:
    servo1.move(sin(t * np.pi / 16) * step_len + init_angles[0] + (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2)
    servo2.move(sin(t * np.pi / 16) * 0 + init_angles[1] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2)
    servo3.move(sin(t * np.pi / 16) * step_len + init_angles[2] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2)

    servo4.move(sin(t * np.pi / 16) * step_len + init_angles[3] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2)
    servo5.move(sin(t * np.pi / 16) * 0 + init_angles[4] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2)
    servo6.move(sin(t * np.pi / 16) * step_len + init_angles[5] + (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2)
    time.sleep(0.01)
    t += 1

    print(t)

    # if t % 16 == 0:
    #     time.sleep(1)
