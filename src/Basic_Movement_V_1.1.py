from fischertechnik.controller.Motor import Motor
from lib.controller import *


def turn_right():
    TXT_M_S2_servomotor.set_position(int(90))
    for count3 in range(5000):
        TXT_M_M1_encodermotor.set_speed(int(450), Motor.CW)
        TXT_M_M1_encodermotor.start_sync()
    TXT_M_S2_servomotor.set_position(int(250))
    for count4 in range(4800):
        TXT_M_M1_encodermotor.set_speed(int(450), Motor.CW)
        TXT_M_M1_encodermotor.start_sync()
    TXT_M_S2_servomotor.set_position(int(180))


TXT_M_S2_servomotor.set_position(int(160))
for count in range(11600):
    TXT_M_M1_encodermotor.set_speed(int(450), Motor.CW)
    TXT_M_M1_encodermotor.start_sync()
TXT_M_S2_servomotor.set_position(int(250))
for count2 in range(7400):
    TXT_M_M1_encodermotor.set_speed(int(450), Motor.CW)
    TXT_M_M1_encodermotor.start_sync()
TXT_M_S2_servomotor.set_position(int(160))