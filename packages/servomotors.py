from __future__ import division
import time
import Adafruit_PCA9685


# from time import sleep

class Servomotors:
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    mouth_GPIO_PIN = 0
    mouth_MIN_ANGLE = 100
    mouth_MIDDLE_ANGLE = 125
    mouth_MAX_ANGLE = 150

    eye_horizontal_GPIO_PIN = 1
    eye_horizontal_MIN_ANGLE = 85
    eye_horizontal_MIDDLE_ANGLE = 95
    eye_horizontal_MAX_ANGLE = 120

    eye_vertical_GPIO_PIN = 2
    eye_vertical_MIN_ANGLE = 100
    eye_vertical_MIDDLE_ANGLE = 120
    eye_vertical_MAX_ANGLE = 120

    head_vertical_GPIO_PIN = 3
    head_vertical_MIN_ANGLE = 20
    head_vertical_MIDDLE_ANGLE = 70
    head_vertical_MAX_ANGLE = 140

    head_horizontal_GPIO_PIN = 4
    head_horizontal_MIN_ANGLE = 40
    head_horizontal_MIDDLE_ANGLE = 85
    head_horizontal_MAX_ANGLE = 130

    def angleToPulse(self, angle):
        pulse = int((angle - 0) * (self.servo_max - self.servo_min) / (180 - 0) + self.servo_min)
        return pulse

    def __init__(self):
        super().__init__()
        self.neutral()

    # All servomotors must be set to middle angle when starting and stopping the application
    # This should be used when starting the InMoov-URI and before turning it off
    def neutral(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        pwm.set_pwm(0, 0, self.angleToPulse(self.head_vertical_MIDDLE_ANGLE))  # Head vertical
        pwm.set_pwm(0, 0, self.angleToPulse(self.head_horizontal_MIDDLE_ANGLE))  # Head horizontal
        pwm.set_pwm(0, 0, self.angleToPulse(self.eye_vertical_MIDDLE_ANGLE))  # Eye vertical
        pwm.set_pwm(0, 0, self.angleToPulse(self.eye_horizontal_MIDDLE_ANGLE))  # Eye horizontal
        pwm.set_pwm(0, 0, self.angleToPulse(self.mouth_MIDDLE_ANGLE))  # Mouth

    def moveTo(self, servomotor, angle):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        pwm.set_pwm(servomotor, 0, self.angleToPulse(angle))

    # THESE FUNCTIONS NEED A SPEED PARAMETER!!!!!!!!!1

    def headUp(self, speed):
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE)
        # for angle in range(self.head_vertical_MIDDLE_ANGLE, self.head_vertical_MAX_ANGLE):
        #    self.moveTo(self.head_vertical_GPIO_PIN, angle)
        # delay

    def headDown(self, speed):
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIN_ANGLE)

    def headLeft(self, speed):
        self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MAX_ANGLE)

    def headRight(self, speed):
        self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MIN_ANGLE)

    def eyesUp(self, speed):
        self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MIN_ANGLE)

    def eyesDown(self, speed):
        self.moveTo(self.eye_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE)

    def eyesLeft(self, speed):
        self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MAX_ANGLE)

    def eyesRight(self, speed):
        self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MIN_ANGLE)

    def mouthClose(self, speed):
        self.moveTo(self.mouth_GPIO_PIN, self.mouth_MIN_ANGLE)

    def mouthOpen(self, speed):
        self.moveTo(self.mouth_GPIO_PIN, self.mouth_MAX_ANGLE)

    def headHorizontalTo(self, speed, angle):
        self.moveTo(self.head_horizontal_GPIO_PIN, angle)

    def headVerticalTo(self, speed, angle):
        self.moveTo(self.head_vertical_GPIO_PIN, angle)

    def eyeHorizontalTo(self, speed, angle):
        self.moveTo(self.eye_horizontal_GPIO_PIN, angle)

    def eyeVerticalTo(self, speed, angle):
        self.moveTo(self.eye_vertical_GPIO_PIN, angle)

    def mouthTo(self,speed, angle):
        self.moveTo(self.mouth_GPIO_PIN, angle)

    def headTo2D(self, speed, xCoord, yCoord):
        self.headHorizontalTo(speed, xCoord)
        self.headVerticalTo(speed, yCoord)

    def eyesTo2D(self, xCoord, yCoord):
        self.eyeHorizontalTo(speed, xCoord)
        self.eyeVerticalTo(speed, yCoord)

# ANIMAÇÕES

# SIM

# NÃO

# TALVEZ

# PESQUISAR MAIS ANIMAÇÕES SIMPLES DE CABEÇAS ROBÓTICAS HUMANOIDES
