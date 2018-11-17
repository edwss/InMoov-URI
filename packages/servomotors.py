from __future__ import division
import time
import Adafruit_PCA9685

# from time import sleep


class Servomotors:
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    mouth_GPIO_PIN = 0
    mouth_lastPosition = 0
    mouth_MIN_ANGLE = 100
    mouth_MIDDLE_ANGLE = 125
    mouth_MAX_ANGLE = 150

    eye_horizontal_GPIO_PIN = 1
    eye_horizontal_lastPosition = 0
    eye_horizontal_MIN_ANGLE = 85
    eye_horizontal_MIDDLE_ANGLE = 95
    eye_horizontal_MAX_ANGLE = 120

    eye_vertical_GPIO_PIN = 2
    eye_vertical_lastPosition = 0
    eye_vertical_MIN_ANGLE = 100
    eye_vertical_MIDDLE_ANGLE = 120
    eye_vertical_MAX_ANGLE = 120

    head_vertical_GPIO_PIN = 3
    head_vertical_lastPosition = 0
    head_vertical_MIN_ANGLE = 20
    head_vertical_MIDDLE_ANGLE = 80
    head_vertical_MAX_ANGLE = 140

    head_horizontal_GPIO_PIN = 4
    head_horizontal_lastPosition = 0
    head_horizontal_MIN_ANGLE = 40
    head_horizontal_MIDDLE_ANGLE = 85
    head_horizontal_MAX_ANGLE = 130

    def angleToPulse(self, angle):
        pulse = int((angle - 0) * (self.servo_max - self.servo_min) / (180 - 0) + self.servo_min)
        return pulse

    def __init__(self):
        super().__init__()
        print("initialising object")
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

        pwm.set_pwm(self.head_vertical_GPIO_PIN, 0, self.angleToPulse(self.head_vertical_MIDDLE_ANGLE))  # Head vertical
        self.head_vertical_lastPosition = self.head_vertical_MIDDLE_ANGLE
        print("Head vertical set to middle!")

        pwm.set_pwm(self.head_horizontal_GPIO_PIN, 0, self.angleToPulse(self.head_horizontal_MIDDLE_ANGLE))  # Head horizontal
        self.head_horizontal_lastPosition = self.head_horizontal_MIDDLE_ANGLE
        print("Head horizontal set to middle!")

        pwm.set_pwm(self.eye_vertical_GPIO_PIN, 0, self.angleToPulse(self.eye_vertical_MIDDLE_ANGLE))  # Eye vertical
        self.eye_vertical_lastPosition = self.eye_vertical_MIDDLE_ANGLE
        print("Eye vertical set to middle!")

        pwm.set_pwm(self.eye_horizontal_GPIO_PIN, 0, self.angleToPulse(self.eye_horizontal_MIDDLE_ANGLE))  # Eye horizontal
        self.eye_horizontal_lastPosition = self.eye_horizontal_MIDDLE_ANGLE
        print("Eye horizontal set to middle!")

        pwm.set_pwm(self.mouth_GPIO_PIN, 0, self.angleToPulse(self.mouth_MIDDLE_ANGLE))  # Mouth
        self.mouth_lastPosition = self.mouth_MIDDLE_ANGLE
        print("Mouth set to middle!")

        print("End initialising!")

    # All servomotors must be set to middle angle when starting and stopping the application
    # This should be used when starting the InMoov-URI and before turning it off
    def neutral(self):
        self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MIDDLE_ANGLE)
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIDDLE_ANGLE)
        self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MIDDLE_ANGLE)
        self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MIDDLE_ANGLE)
        self.moveTo(self.mouth_GPIO_PIN, self.mouth_MIDDLE_ANGLE)

    def moveTo(self, servomotor, angle, speed):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

        if servomotor == self.mouth_GPIO_PIN:
            if angle < self.mouth_MIN_ANGLE | angle > self.mouth_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Moving mouth to: ", angle)
            for x in range(self.mouth_lastPosition, angle):
                pwm.set_pwm(self.mouth_GPIO_PIN, 0, self.angleToPulse(x))
                self.mouth_lastPosition = x
                time.sleep(speed)

        elif servomotor == self.head_horizontal_GPIO_PIN:
            if angle < self.head_horizontal_MIN_ANGLE | angle > self.head_horizontal_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Moving head horizontal to: ", angle)
            for x in range(self.head_horizontal_lastPosition, angle):
                pwm.set_pwm(self.head_horizontal_GPIO_PIN, 0, self.angleToPulse(x))
                self.head_horizontal_lastPosition = x
                time.sleep(speed)

        elif servomotor == self.head_vertical_GPIO_PIN:
            if angle < self.head_vertical_MIN_ANGLE | angle > self.head_vertical_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Moving head vertical to: ", angle)
            for x in range(self.head_vertical_GPIO_PIN, angle):
                pwm.set_pwm(self.head_vertical_GPIO_PIN, 0, self.angleToPulse(x))
                self.head_vertical_lastPosition = x
                time.sleep(speed)

        elif servomotor == self.eye_horizontal_GPIO_PIN:
            if angle < self.eye_horizontal_MIN_ANGLE | angle > self.eye_horizontal_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Moving eye horizontal to: ", angle)
            for x in range(self.eye_horizontal_lastPosition, angle):
                pwm.set_pwm(self.eye_horizontal_GPIO_PIN, 0, self.angleToPulse(x))
                self.eye_horizontal_lastPosition = x
                time.sleep(speed)

        elif servomotor == self.eye_vertical_GPIO_PIN:
            if angle < self.eye_vertical_MIN_ANGLE | angle > self.eye_vertical_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Moving eye vertical to: ", angle)
            for x in range(self.eye_vertical_lastPosition, angle):
                pwm.set_pwm(self.eye_vertical_GPIO_PIN, 0, self.angleToPulse(x))
                self.eye_vertical_lastPosition = x
                time.sleep(speed)

        else:
            raise Exception("The given servomotor is invalid!")

        # pwm.set_pwm(servomotor, 0, self.angleToPulse(angle))

    def headUp(self, speed):
        # self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE)
        print("Moving head up...")
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE, speed)
        print("Head up!")

    def headDown(self, speed):
        # self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIN_ANGLE)
        print("Moving head down...")
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIN_ANGLE, speed)
        print("Head down!")

    def headLeft(self, speed):
        # self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MAX_ANGLE)
        for angle in range(self.head_horizontal_lastPosition, self.head_horizontal_MAX_ANGLE):
            self.moveTo(self.head_horizontal_GPIO_PIN, angle)
            self.head_horizontal_lastPosition = angle
            time.sleep(float(speed))

    def headRight(self, speed):
        # self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MIN_ANGLE)
        for angle in range(self.head_horizontal_lastPosition, self.head_horizontal_MIN_ANGLE):
            self.moveTo(self.head_horizontal_GPIO_PIN, angle)
            self.head_horizontal_lastPosition = angle
            time.sleep(float(speed))

    def eyesUp(self, speed):
        # self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MIN_ANGLE)
        for angle in range(self.eye_vertical_lastPosition, self.eye_vertical_MIN_ANGLE):
            self.moveTo(self.eye_vertical_GPIO_PIN, angle)
            self.eye_vertical_lastPosition = angle
            time.sleep(float(speed))

    def eyesDown(self, speed):
        # self.moveTo(self.eye_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE)
        for angle in range(self.eye_vertical_lastPosition, self.eye_vertical_MAX_ANGLE):
            self.moveTo(self.eye_vertical_GPIO_PIN, angle)
            self.eye_vertical_lastPosition = angle
            time.sleep(float(speed))

    def eyesLeft(self, speed):
        # self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MAX_ANGLE)
        for angle in range(self.eye_horizontal_lastPosition, self.eye_horizontal_MAX_ANGLE):
            self.moveTo(self.eye_horizontal_GPIO_PIN, angle)
            self.eye_horizontal_lastPosition = angle
            time.sleep(float(speed))

    def eyesRight(self, speed):
        # self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MIN_ANGLE)
        for angle in range(self.eye_horizontal_lastPosition, self.eye_horizontal_MIN_ANGLE):
            self.moveTo(self.eye_horizontal_GPIO_PIN, angle)
            self.eye_horizontal_lastPosition = angle
            time.sleep(float(speed))

    def mouthClose(self, speed):
        # self.moveTo(self.mouth_GPIO_PIN, self.mouth_MIN_ANGLE)
        for angle in range(self.mouth_lastPosition, self.mouth_MIN_ANGLE):
            self.moveTo(self.mouth_GPIO_PIN, angle)
            self.mouth_lastPosition = angle
            time.sleep(float(speed))

    def mouthOpen(self, speed):
        # self.moveTo(self.mouth_GPIO_PIN, self.mouth_MAX_ANGLE)
        for angle in range(self.mouth_lastPosition, self.mouth_MAX_ANGLE):
            self.moveTo(self.mouth_GPIO_PIN, angle)
            self.mouth_lastPosition = angle
            time.sleep(float(speed))

    def headHorizontalTo(self, speed, angleTo):
        # self.moveTo(self.head_horizontal_GPIO_PIN, angle)
        for angle in range(self.head_horizontal_lastPosition, angleTo):
            self.moveTo(self.head_horizontal_GPIO_PIN, angle)
            self.head_horizontal_lastPosition = angle
            time.sleep(float(speed))

    def headVerticalTo(self, speed, angleTo):
        # self.moveTo(self.head_vertical_GPIO_PIN, angle)
        for angle in range(self.head_vertical_lastPosition, angleTo):
            self.moveTo(self.head_vertical_GPIO_PIN, angle)
            self.head_vertical_lastPosition = angle
            time.sleep(float(speed))

    def eyeHorizontalTo(self, speed, angleTo):
        # self.moveTo(self.eye_horizontal_GPIO_PIN, angle)
        for angle in range(self.eye_horizontal_lastPosition, angleTo):
            self.moveTo(self.eye_horizontal_GPIO_PIN, angle)
            self.eye_horizontal_lastPosition = angle
            time.sleep(float(speed))

    def eyeVerticalTo(self, speed, angleTo):
        # self.moveTo(self.eye_vertical_GPIO_PIN, angle)
        for angle in range(self.eye_vertical_lastPosition, angleTo):
            self.moveTo(self.eye_vertical_GPIO_PIN, angle)
            self.eye_vertical_lastPosition = angle
            time.sleep(float(speed))

    def mouthTo(self,speed, angleTo):
        # self.moveTo(self.mouth_GPIO_PIN, angle)
        for angle in range(self.mouth_lastPosition, angleTo):
            self.moveTo(self.mouth_GPIO_PIN, angle)
            self.mouth_lastPosition = angle
            time.sleep(float(speed))

    def headTo2D(self, speed, xCoord, yCoord):
        self.headHorizontalTo(speed, xCoord)
        self.headVerticalTo(speed, yCoord)

    def eyesTo2D(self, speed, xCoord, yCoord):
        self.eyeHorizontalTo(speed, xCoord)
        self.eyeVerticalTo(speed, yCoord)

# ANIMAÇÕES

# SIM

# NÃO

# TALVEZ

# PESQUISAR MAIS ANIMAÇÕES SIMPLES DE CABEÇAS ROBÓTICAS HUMANOIDES
