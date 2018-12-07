from __future__ import division
import time
import Adafruit_PCA9685


class Servomotor:

    # Tamanho mínimo e máximo do pulso do PCA9685
    servo_min_pulse_length = 150  # Min pulse length out of 4096
    servo_max_pulse_length = 600  # Max pulse length out of 4096

    servo_PIN = 0
    servo_last_position = 0
    servo_min_angle = 0
    servo_middle_angle = 0
    servo_max_angle = 0

    def angleToPulse(self, angle):
        pulse = int((angle - 0) * (self.servo_max_pulse_length - self.servo_min_pulse_length) / (180 - 0) + self.servo_min_pulse_length)
        return pulse

    def __init__(self, servo_pin, servo_min_angle, servo_middle_angle, servo_max_angle):
        super().__init__()
        print("initialising object")
        pwm = Adafruit_PCA9685.PCA9685()  # Instanciação do objeto PCA9685
        pwm.set_pwm_freq(60)  # Frequência de comunicação com o barramento - 60Hz
        self.servo_PIN = servo_pin
        self.servo_min_angle = servo_min_angle
        self.servo_middle_angle = servo_middle_angle
        self.servo_max_angle = servo_max_angle
        self.neutral(0.05)

    def moveTo(self, angle, speed):
        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

        if angle < self.servo_min_angle or angle > self.servo_max_angle:
            raise Exception("The given angle value is lesser or bigger than servo capabilities!")

        if self.servo_last_position > angle:
            for x in range(self.servo_last_position, angle, -1):
                print("Angle now: ", x)
                pwm.set_pwm(self.servo_PIN, 0, self.angleToPulse(x))
                self.servo_last_position = x
                time.sleep(speed)
        else:
            for x in range(self.servo_last_position, angle):
                print("Angle now: ", x)
                pwm.set_pwm(self.servo_PIN, 0, self.angleToPulse(x))
                self.servo_last_position = x
                time.sleep(speed)

    def neutral(self, speed):
        self.moveTo(self.servo_middle_angle, speed)


class Head(Servomotor):

    # Constantes do servomotor da boca
    mouth_GPIO_PIN = 0
    mouth_MIN_ANGLE = 100
    mouth_MIDDLE_ANGLE = 125
    mouth_MAX_ANGLE = 150
    mouth = None
    mouth_lastPosition = 0

    # Constantes do servomotor da olho horizontal
    eye_horizontal_GPIO_PIN = 1
    eye_horizontal_MIN_ANGLE = 85
    eye_horizontal_MIDDLE_ANGLE = 95
    eye_horizontal_MAX_ANGLE = 120
    eye_horizontal = None
    eye_horizontal_lastPosition = 0

    # Constantes do servomotor da olho vertical
    eye_vertical_GPIO_PIN = 2
    eye_vertical_MIN_ANGLE = 100
    eye_vertical_MIDDLE_ANGLE = 120
    eye_vertical_MAX_ANGLE = 120
    eye_vertical = None
    eye_vertical_lastPosition = 0

    # Constantes do servomotor da cabeça vertical
    head_vertical_GPIO_PIN = 3
    head_vertical_MIN_ANGLE = 20
    head_vertical_MIDDLE_ANGLE = 80
    head_vertical_MAX_ANGLE = 140
    head_vertical = None
    head_vertical_lastPosition = 0

    # Constantes do servomotor da cabeça horizontal
    head_horizontal_GPIO_PIN = 4
    head_horizontal_MIN_ANGLE = 40
    head_horizontal_MIDDLE_ANGLE = 85
    head_horizontal_MAX_ANGLE = 130
    head_horizontal = None
    head_horizontal_lastPosition = 0

    def __init__(self, servo_pin, servo_min_angle, servo_middle_angle, servo_max_angle):
        super().__init__(servo_pin, servo_min_angle, servo_middle_angle, servo_max_angle)
        self.initialise()

    def initialise(self):
        # instancia os objetos com os parâmetros previamente definidos
        self.mouth = Servomotor(self.mouth_GPIO_PIN, self.mouth_MIN_ANGLE, self.mouth_MIDDLE_ANGLE, self.mouth_MAX_ANGLE)
        self.head_vertical = Servomotor(self.head_vertical_GPIO_PIN, self.head_vertical_MIN_ANGLE, self.head_vertical_MIDDLE_ANGLE, self.head_vertical_MAX_ANGLE)
        self.head_horizontal = Servomotor(self.head_horizontal_GPIO_PIN, self.head_horizontal_MIN_ANGLE, self.head_horizontal_MIDDLE_ANGLE, self.head_horizontal_MAX_ANGLE)
        self.eye_vertical = Servomotor(self.eye_vertical_GPIO_PIN, self.eye_vertical_MIN_ANGLE, self.eye_vertical_MIDDLE_ANGLE, self.eye_vertical_MAX_ANGLE)
        self.eye_horizontal = Servomotor(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MIN_ANGLE, self.eye_horizontal_MIDDLE_ANGLE, self.eye_horizontal_MAX_ANGLE)

        # move eles para a posição neutra
        self.mouth.neutral(0.05)
        self.head_vertical.neutral(0.05)
        self.head_horizontal.neutral(0.05)
        self.eye_vertical.neutral(0.05)
        self.eye_horizontal.neutral(0.05)

    # Move o eixo vertical da cabeça robótica para cima
    def Up(self, speed):
        self.head_vertical.moveTo(self.head_vertical_MAX_ANGLE, speed)

    # Move o eixo vertical da cabeça robótica para baixo
    def Down(self, speed):
        self.head_vertical.moveTo(self.head_vertical_MIN_ANGLE, speed)

    # Move o eixo horizontal da cabeça robótica para esquerda
    def Left(self, speed):
        self.head_horizontal.moveTo(self.head_horizontal_MAX_ANGLE, speed)

    # Move o eixo horizontal da cabeça robótica para direita
    def Right(self, speed):
        self.head_horizontal.moveTo(self.head_horizontal_MIN_ANGLE, speed)