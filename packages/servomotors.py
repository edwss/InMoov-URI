from __future__ import division
import time
import Adafruit_PCA9685
#from time import sleep

class Servomotors:

    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    mouth_GPIO_PIN = 0
    mouth_MIN_ANGLE = 0
    mouth_MIDDLE_ANGLE = 0
    mouth_MAX_ANGLE = 0

    left_eye_GPIO_PIN = 1
    left_eye_MIN_ANGLE = 0
    left_eye_MIDDLE_ANGLE = 0
    left_eye_MAX_ANGLE = 0

    right_eye_GPIO_PIN = 2
    right_eye_MIN_ANGLE = 0
    right_eye_MIDDLE_ANGLE = 0
    right_eye_MAX_ANGLE = 0

    vertical_head_GPIO_PIN = 3
    vertical_head_MIN_ANGLE = 20
    vertical_head_MIDDLE_ANGLE = 0
    vertical_head_MAX_ANGLE = 140

    horizontal_head_GPIO_PIN = 4
    horizontal_head_MIN_ANGLE = 0
    horizontal_head_MIDDLE_ANGLE = 0
    horizontal_head_MAX_ANGLE = 0

    def angleToPulse(self, angle):
        pulse = int((angle - 0) * (self.servo_max - self.servo_min) / (180 - 0) + self.servo_min)
        return pulse

    def __init__(self):
        super().__init__()

        self.neutral()

    # All servomotors must be set to middle angle when starting and stopping the application
    # This should be used when starting the InMoov and before turning it off
    def neutral(self):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        pwm.set_pwm(0, 0, self.angleToPulse(CONSTANTE??)) #Head vertical
        pwm.set_pwm(0, 0, self.angleToPulse(CONSTANTE??)) #Head horizontal
        pwm.set_pwm(0, 0, self.angleToPulse(CONSTANTE??)) #Eye vertical
        pwm.set_pwm(0, 0, self.angleToPulse(CONSTANTE??)) #Eye horizontal
        pwm.set_pwm(0, 0, self.angleToPulse(CONSTANTE??)) #Mouth

    def moveTo(self, servomotor, angle):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)
        pwm.set_pwm(servomotor, 0, self.angleToPulse(angle))

#THESE FUNCTIONS NEED A SPEED PARAMETER!!!!!!!!!1

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

    def headHorizontalTo(self,angle):

    def headVerticalTo(self, angle):

    def eyeHorizontalTo(self,angle):

    def eyeVerticalTo(self, angle):

    def mouthTo(self,angle):

    def headTo2D(self, xCoord, yCoord):

    def eyesTo2D(self, xCoord, yCoord):


#ANIMAÇÕES

#SIM

#NÃO

#TALVEZ

#PESQUISAR MAIS ANIMAÇÕES SIMPLES DE CABEÇAS ROBÓTICAS HUMANOIDES






