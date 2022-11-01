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

servo_list = [servo1, servo2, servo3, servo4, servo5, servo6]

class bipedal():
    def __init__(self, init_a, center_height):
        self.init_angle = init_a
        self.curr_angle = init_a
        self.c_height = center_height

    def direct_move_six(self, new_a):
        for i in range(6):
            servo_list[i].move(new_a[i])

        self.curr_angle = new_a

    def boot(self):
        target_a = []
        for i in range(6):
            target_a.append(self.init_angle[i] + self.c_height[i])
        self.sin_move_six(target_a, 20)
        print("boot")

    def sin_move_six(self, new_a, num_steps):
        for step in range(num_steps + 1):
            for i in range(6):
                servo_list[i].move((new_a[i] - self.curr_angle[i]) * (1-np.cos(step * np.pi / num_steps)) / 2 + self.curr_angle[i])
                time.sleep(0.01)

        self.curr_angle = new_a

    def home(self):
        self.sin_move_six(self.init_angle, 20)
        print("home")

def move_steps(robot step_len, steps, height):
    t = 0
    up_angle = start_angle-height
    while t<16*steps:
        angle_list = [
            sin(t * np.pi / 16) * step_len + init_angles[0] + (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2,
            sin(t * np.pi / 16) * 0 + init_angles[1] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2,
            sin(t * np.pi / 16) * step_len + init_angles[2] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2,
            sin(t * np.pi / 16) * step_len + init_angles[3] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2,
            sin(t * np.pi / 16) * 0 + init_angles[4] - (start_angle - up_angle)/2 * cos(t * np.pi / 16) + (start_angle + up_angle)/2,
            sin(t * np.pi / 16) * step_len + init_angles[5] + (start_angle - up_angle)/2 * cos(t * np.pi / 16) - (start_angle + up_angle)/2
        ]
        robot.direct_move_six(angle_list)
        time.sleep(0.01)
        t += 1


if __name__ == "__main__":
    time.sleep(5)
    # move_steps(step_len=0, steps=10, height=5)
    # move_steps(step_len=1, steps=10, height=8)
    # move_steps(step_len=2, steps=10, height=10)
    # move_steps(step_len=3, steps=10, height=10)
    # move_steps(step_len=4, steps=50, height=10)
    # move_steps(step_len=2, steps=10, height=10)

    h = 10
    c_h = 30
    start_angle = 40
    init_angles = np.array([32, 230, 232, 40, 20, 205])
    init_add_height = np.array([32 + h, 230 - h, 232 - h, 40 + h, 20 + h, 205 - h])
    height_list = np.array([c_h, -c_h, -c_h, c_h, c_h, -c_h])
    
    my_biped = bipedal(init_a=init_add_height, center_height=height_list)
    my_biped.boot()
    
    move_steps(robot=my_biped, step_len=0, steps=10, height=5)
    move_steps(robot=my_biped, step_len=1, steps=10, height=8)

    my_biped.home()






