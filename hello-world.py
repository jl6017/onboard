import sys
from math import sin, cos
from lx16a import *
import time
import numpy as np

# LX16A.initialize("/dev/cu.usbserial-2130", 0.1)
LX16A.initialize("/dev/ttyUSB0", 0.1)

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
    print("Servo {e.id_} is not responding. Exiting...")
    quit()

start_angle = 40
init_angles = [32, 230, 232, 40, 20, 205]

class bipedal():
    def __init__(self, init_a):
        self.curr = init_a
        ##  to do

def move_steps(step_len, steps, height):
    t = 0
    up_angle = start_angle-height
    while t<16*steps:
        servo1.move(sin(t * np.pi / 16) * step_len + init_angles[0] + (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2)
        servo2.move(sin(t * np.pi / 16) * 0 + init_angles[1] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2)
        servo3.move(sin(t * np.pi / 16) * step_len + init_angles[2] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2)

        servo4.move(sin(t * np.pi / 16) * step_len + init_angles[3] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2)
        servo5.move(sin(t * np.pi / 16) * 0 + init_angles[4] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2)
        servo6.move(sin(t * np.pi / 16) * step_len + init_angles[5] + (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2)
        time.sleep(0.01)
        t += 1

        print(t)

def start_pos(angle_list):
    servo1.move(angle_list[0])
    servo2.move(angle_list[1])
    servo3.move(angle_list[2])
    servo4.move(angle_list[3])
    servo5.move(angle_list[4])
    servo6.move(angle_list[5])


if __name__ == "__main__":
    time.sleep(5)
    move_steps(step_len=0, steps=10, height=5)
    move_steps(step_len=1, steps=10, height=8)
    move_steps(step_len=2, steps=10, height=10)
    move_steps(step_len=3, steps=10, height=10)
    move_steps(step_len=4, steps=50, height=10)
    move_steps(step_len=2, steps=10, height=10)
    
    # start_pos(init_angles)
    print("done")






