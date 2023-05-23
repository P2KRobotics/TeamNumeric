
import time

from fischertechnik.controller.Motor import Motor
from lib.camera import *
from lib.controller import *


right_turn = None
red_value = None
green_value = None
blue_value = None
straight = None
left_turn = None


def color_callback(event):
    global right_turn, red_value, green_value, blue_value, straight, left_turn
    red_value = event.value.get_rgb_red()
    green_value = event.value.get_rgb_green()
    blue_value = event.value.get_rgb_blue()


color_detector.add_detection_listener(color_callback)


red_value = 0
green_value = 0
blue_value = 0
straight = 300
right_turn = 90
left_turn = 90
TXT_M_S1_servomotor.set_position(int(160))
time.sleep(1)
TXT_M_S1_servomotor.set_position(int(straight))
time.sleep(2)
while True:
    TXT_M_M1_encodermotor.set_speed(int(300), Motor.CW)
    TXT_M_M1_encodermotor.start_sync()
    if red_value > 10:
        if green_value < 70 and blue_value < 70 and red_value > 100:
            TXT_M_M1_encodermotor.set_speed(int(300), Motor.CCW)
            TXT_M_M1_encodermotor.start_sync()
            time.sleep(2)
    time.sleep(0.2)