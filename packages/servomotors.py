from __future__ import division
import time
import Adafruit_PCA9685


class Servomotors:

    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    mouth_GPIO_PIN = 10
    mouth_MIN_ANGLE = 0
    mouth_MIDDLE_ANGLE = 0
    mouth_MAX_ANGLE = 0

    left_eye_GPIO_PIN = 11
    left_eye_MIN_ANGLE = 0
    left_eye_MIDDLE_ANGLE = 0
    left_eye_MAX_ANGLE = 0

    right_eye_GPIO_PIN = 12
    right_eye_MIN_ANGLE = 0
    right_eye_MIDDLE_ANGLE = 0
    right_eye_MAX_ANGLE = 0

    vertical_head_GPIO_PIN = 13
    vertical_head_MIN_ANGLE = 0
    vertical_head_MIDDLE_ANGLE = 0
    vertical_head_MAX_ANGLE = 0

    horizontal_head_GPIO_PIN = 14
    horizontal_head_MIN_ANGLE = 0
    horizontal_head_MIDDLE_ANGLE = 0
    horizontal_head_MAX_ANGLE = 0

     def angleToPulse(self, angle):
         pulse = (angle - 0) * (servo_max - servo_min) / (180 - 0) + servo_min
         return pulse

    def __init__(self):
        super().__init__()
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        self.neutral()

    # Here I'll have to set all servomotors to middle angle.
    # This should be used when starting the InMoov and before turning it off
    def neutral(self):

    def headUp(self, angle):

    def headDown(self, angle):

    def headLeft(self, angle):

    def headRight(self, angle):

    def eyesUp(self, angle):

    def eyesDown(self, angle):

    def eyesLeft(self, angle):

    def eyesRight(self, angle):

    def closeMouth(self):

    def mouthAngle(self, angle):












