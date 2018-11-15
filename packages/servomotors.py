from __future__ import division
import time
import Adafruit_PCA9685
#from time import sleep

class Servomotors:

    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    mouth_GPIO_PIN = 0
    mouth_MIN_ANGLE = 105
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
    head_horizontal_MIN_ANGLE = 25
    head_horizontal_MIDDLE_ANGLE = 88
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
        pwm.set_pwm(0, 0, self.angleToPulse(self.head_vertical_MIDDLE_ANGLE)) #Head vertical
        pwm.set_pwm(0, 0, self.angleToPulse(self.head_horizontal_MIDDLE_ANGLE)) #Head horizontal
        pwm.set_pwm(0, 0, self.angleToPulse(self.eye_vertical_MIDDLE_ANGLE)) #Eye vertical
        pwm.set_pwm(0, 0, self.angleToPulse(self.eye_horizontal_MIDDLE_ANGLE)) #Eye horizontal
        pwm.set_pwm(0, 0, self.angleToPulse(self.mouth_MIDDLE_ANGLE)) #Mouth

    def moveTo(self, servomotor, angle):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        pwm.set_pwm(servomotor, 0, self.angleToPulse(angle))

#THESE FUNCTIONS NEED A SPEED PARAMETER!!!!!!!!!1

    def headUp(self, speed):
        for angle in range(self.head_vertical_MIDDLE_ANGLE, self.head_vertical_MAX_ANGLE):
            self.moveTo(self.head_vertical_GPIO_PIN, angle)
        #delay
        #self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE)

    def headDown(self, speed):
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIN_ANGLE)

    def headLeft(self, speed):
        self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MAX_ANGLE)

    # def headRight(self, angle):

    # def eyesUp(self, angle):
    #
    # def eyesDown(self, angle):
    #
    # def eyesLeft(self, angle):
    #
    # def eyesRight(self, angle):
    #
    # def mouthClose(self):
    #
    # def mouthOpen(self, angle):
    #
    # def headHorizontalTo(self,angle):
    #
    # def headVerticalTo(self, angle):
    #
    # def eyeHorizontalTo(self,angle):
    #
    # def eyeVerticalTo(self, angle):
    #
    # def mouthTo(self,angle):
    #
    # def headTo2D(self, xCoord, yCoord):
    #
    # def eyesTo2D(self, xCoord, yCoord):


#ANIMAÇÕES

#SIM

#NÃO

#TALVEZ

#PESQUISAR MAIS ANIMAÇÕES SIMPLES DE CABEÇAS ROBÓTICAS HUMANOIDES






