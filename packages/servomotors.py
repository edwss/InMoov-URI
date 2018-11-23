from __future__ import division
import time
import Adafruit_PCA9685


class Servomotors:

    # Tamanho mínimo e máximo do pulso do PCA9685
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    # Constantes do servomotor da boca
    mouth_GPIO_PIN = 0
    mouth_lastPosition = 0
    mouth_MIN_ANGLE = 100
    mouth_MIDDLE_ANGLE = 125
    mouth_MAX_ANGLE = 150

    # Constantes do servomotor da olho horizontal
    eye_horizontal_GPIO_PIN = 1
    eye_horizontal_lastPosition = 0
    eye_horizontal_MIN_ANGLE = 85
    eye_horizontal_MIDDLE_ANGLE = 95
    eye_horizontal_MAX_ANGLE = 120

    # Constantes do servomotor da olho vertical
    eye_vertical_GPIO_PIN = 2
    eye_vertical_lastPosition = 0
    eye_vertical_MIN_ANGLE = 100
    eye_vertical_MIDDLE_ANGLE = 120
    eye_vertical_MAX_ANGLE = 120

    # Constantes do servomotor da cabeça vertical
    head_vertical_GPIO_PIN = 3
    head_vertical_lastPosition = 0
    head_vertical_MIN_ANGLE = 20
    head_vertical_MIDDLE_ANGLE = 80
    head_vertical_MAX_ANGLE = 140

    # Constantes do servomotor da cabeça horizontal
    head_horizontal_GPIO_PIN = 4
    head_horizontal_lastPosition = 0
    head_horizontal_MIN_ANGLE = 40
    head_horizontal_MIDDLE_ANGLE = 85
    head_horizontal_MAX_ANGLE = 130

    # Função que converte valores entre 0 e 180 graus para o correspondente pulso para o PCA9685
    def angleToPulse(self, angle):
        pulse = int((angle - 0) * (self.servo_max - self.servo_min) / (180 - 0) + self.servo_min)
        return pulse

    # Inicialização da classe
    def __init__(self):
        super().__init__()
        print("initialising object")
        pwm = Adafruit_PCA9685.PCA9685() # Instanciação do objeto PCA9685
        pwm.set_pwm_freq(60) # Frequência de comunicação com o barramento - 60Hz

        # Essas funções deixam os servomotores na posição neutra deles (MIDDLE)
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

    # Essa função deixa os motores na posição neutra, com uma velocidade de entrada
    def neutral(self, speed):
        self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MIDDLE_ANGLE, speed)
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIDDLE_ANGLE, speed)
        self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MIDDLE_ANGLE, speed)
        self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MIDDLE_ANGLE, speed)
        self.moveTo(self.mouth_GPIO_PIN, self.mouth_MIDDLE_ANGLE, speed)

    # Função para mover os servomotores dado o pino dele, o ângulo e a velocidade
    def moveTo(self, servomotor, angle, speed):

        pwm = Adafruit_PCA9685.PCA9685()
        pwm.set_pwm_freq(60)

        # Cada um dessas condições if é para um servomotor diferente
        if servomotor == self.mouth_GPIO_PIN:
            print("Angle: ", angle, "Min: ", self.mouth_MIN_ANGLE, " Max: ", self.mouth_MAX_ANGLE)
            # Aqui tem uma checagem do parâmetro ângulo passado a função.
            # Caso exceda os limites, uma exception é chamada.
            if angle < self.mouth_MIN_ANGLE or angle > self.mouth_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Last Position: ", self.mouth_lastPosition)
            print("Moving mouth to: ", angle)

            if self.mouth_lastPosition > angle:
                for x in range(self.mouth_lastPosition, angle, -1):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.mouth_GPIO_PIN, 0, self.angleToPulse(x))
                    self.mouth_lastPosition = x
                    time.sleep(speed)
            else:
                for x in range(self.mouth_lastPosition, angle):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.mouth_GPIO_PIN, 0, self.angleToPulse(x))
                    self.mouth_lastPosition = x
                    time.sleep(speed)

        elif servomotor == self.head_horizontal_GPIO_PIN:
            print("Angle: ", angle, "Min: ", self.head_horizontal_MIN_ANGLE, " Max: ", self.head_horizontal_MAX_ANGLE)
            if angle < self.head_horizontal_MIN_ANGLE or angle > self.head_horizontal_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Last Position: ", self.head_horizontal_lastPosition)
            print("Moving head horizontal to: ", angle)

            if self.head_horizontal_lastPosition > angle:
                for x in range(self.head_horizontal_lastPosition, angle, -1):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.head_horizontal_GPIO_PIN, 0, self.angleToPulse(x))
                    self.head_horizontal_lastPosition = x
                    time.sleep(speed)
            else:
                for x in range(self.head_horizontal_lastPosition, angle):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.head_horizontal_GPIO_PIN, 0, self.angleToPulse(x))
                    self.head_horizontal_lastPosition = x
                    time.sleep(speed)

        elif servomotor == self.head_vertical_GPIO_PIN:
            print("Angle: ", angle, "Min: ", self.head_vertical_MIN_ANGLE, " Max: ", self.head_vertical_MAX_ANGLE)
            if angle < self.head_vertical_MIN_ANGLE or angle > self.head_vertical_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Last Position: ", self.head_vertical_lastPosition)
            print("Moving head vertical to: ", angle)

            if self.head_vertical_lastPosition > angle:
                for x in range(self.head_vertical_lastPosition, angle, -1):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.head_vertical_GPIO_PIN, 0, self.angleToPulse(x))
                    self.head_vertical_lastPosition = x
                    time.sleep(speed)
            else:
                for x in range(self.head_vertical_lastPosition, angle):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.head_vertical_GPIO_PIN, 0, self.angleToPulse(x))
                    self.head_vertical_lastPosition = x
                    time.sleep(speed)

        elif servomotor == self.eye_horizontal_GPIO_PIN:
            print("Angle: ", angle, "Min: ", self.eye_horizontal_MIN_ANGLE, " Max: ", self.eye_horizontal_MAX_ANGLE)
            if angle < self.eye_horizontal_MIN_ANGLE or angle > self.eye_horizontal_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Last Position: ", self.eye_horizontal_lastPosition)
            print("Moving eye horizontal to: ", angle)

            if self.eye_horizontal_lastPosition > angle:
                for x in range(self.eye_horizontal_lastPosition, angle, -1):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.eye_horizontal_GPIO_PIN, 0, self.angleToPulse(x))
                    self.eye_horizontal_lastPosition = x
                    time.sleep(speed)
            else:
                for x in range(self.eye_horizontal_lastPosition, angle):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.eye_horizontal_GPIO_PIN, 0, self.angleToPulse(x))
                    self.eye_horizontal_lastPosition = x
                    time.sleep(speed)

        elif servomotor == self.eye_vertical_GPIO_PIN:
            print("Angle: ", angle, "Min: ", self.eye_vertical_MIN_ANGLE, " Max: ", self.eye_vertical_MAX_ANGLE)
            if angle < self.eye_vertical_MIN_ANGLE or angle > self.eye_vertical_MAX_ANGLE:
                raise Exception("The given angle value is lesser or bigger than servo capabilities!")
            print("Last Position: ", self.eye_vertical_lastPosition)
            print("Moving eye vertical to: ", angle)

            if self.eye_vertical_lastPosition > angle:
                for x in range(self.eye_vertical_lastPosition, angle, -1):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.eye_vertical_GPIO_PIN, 0, self.angleToPulse(x))
                    self.eye_vertical_lastPosition = x
                    time.sleep(speed)
            else:
                for x in range(self.eye_vertical_lastPosition, angle):
                    print("Angle now: ", x)
                    pwm.set_pwm(self.eye_vertical_GPIO_PIN, 0, self.angleToPulse(x))
                    self.eye_vertical_lastPosition = x
                    time.sleep(speed)

        else:
            raise Exception("The given servomotor is invalid!")

        # pwm.set_pwm(servomotor, 0, self.angleToPulse(angle))

    # Move o eixo vertical da cabeça robótica para cima
    def headUp(self, speed):
        # self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE)
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MAX_ANGLE, speed)

    # Move o eixo vertical da cabeça robótica para baixo
    def headDown(self, speed):
        # self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIN_ANGLE)
        self.moveTo(self.head_vertical_GPIO_PIN, self.head_vertical_MIN_ANGLE, speed)

    # Move o eixo horizontal da cabeça robótica para esquerda
    def headLeft(self, speed):
        # self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MAX_ANGLE)
        self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MAX_ANGLE, speed)

    # Move o eixo horizontal da cabeça robótica para direita
    def headRight(self, speed):
        # self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MIN_ANGLE)
        self.moveTo(self.head_horizontal_GPIO_PIN, self.head_horizontal_MIN_ANGLE, speed)

    # Move o eixo vertical dos olhos robótica para cima
    def eyesUp(self, speed):
        # self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MIN_ANGLE)
        self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MIN_ANGLE, speed)

    # Move o eixo vertical dos olhos robótica para baixo
    def eyesDown(self, speed):
        # self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MAX_ANGLE)
        self.moveTo(self.eye_vertical_GPIO_PIN, self.eye_vertical_MAX_ANGLE, speed)

    # Move o eixo horizontal dos olhos robótica para esquerda
    def eyesLeft(self, speed):
        # self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MAX_ANGLE)
        self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MAX_ANGLE, speed)

    # Move o eixo horizontal dos olhos robótica para direita
    def eyesRight(self, speed):
        # self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MIN_ANGLE)
        self.moveTo(self.eye_horizontal_GPIO_PIN, self.eye_horizontal_MIN_ANGLE, speed)

    # Move o eixo vertical da boca robótica para cima (fechando-a)
    def mouthClose(self, speed):
        # self.moveTo(self.mouth_GPIO_PIN, self.mouth_MIN_ANGLE)
        self.moveTo(self.mouth_GPIO_PIN, self.mouth_MIN_ANGLE, speed)

    # Move o eixo vertical da boca robótica para baixo (abrindo-a)
    def mouthOpen(self, speed):
        # self.moveTo(self.mouth_GPIO_PIN, self.mouth_MAX_ANGLE)
        self.moveTo(self.mouth_GPIO_PIN, self.mouth_MAX_ANGLE, speed)

    # Move o eixo horizontal da cabeça robótica para um ângulo definido pelo usuário
    def headHorizontalTo(self, speed, angleTo):
        # self.moveTo(self.head_horizontal_GPIO_PIN, angle)
        self.moveTo(self.head_horizontal_GPIO_PIN, angleTo, speed)

    # Move o eixo vertical da cabeça robótica para um ângulo definido pelo usuário
    def headVerticalTo(self, speed, angleTo):
        # self.moveTo(self.head_vertical_GPIO_PIN, angle)
        self.moveTo(self.head_vertical_GPIO_PIN, angleTo, speed)

    # Move o eixo horizontal dos olhos para um ângulo definido pelo usuário
    def eyeHorizontalTo(self, speed, angleTo):
        # self.moveTo(self.eye_horizontal_GPIO_PIN, angle)
        self.moveTo(self.eye_horizontal_GPIO_PIN, angleTo, speed)

    # Move o eixo vertical dos olhos para um ângulo definido pelo usuário
    def eyeVerticalTo(self, speed, angleTo):
        # self.moveTo(self.eye_vertical_GPIO_PIN, angle)
        self.moveTo(self.eye_vertical_GPIO_PIN, angleTo, speed)

    # # Move o eixo vertical da boca para um ângulo definido pelo usuário
    # def mouthTo(self, speed, angleTo):
    #     # self.moveTo(self.mouth_GPIO_PIN, angle)
    #     for angle in range(self.mouth_lastPosition, angleTo):
    #         self.moveTo(self.mouth_GPIO_PIN, angle)
    #         self.mouth_lastPosition = angle
    #         time.sleep(float(speed))

    # Move os eixos vertical e horizontal da cabeça para uma coordenada definida pelo usuário
    def headTo2D(self, speed, xCoord, yCoord):
        self.headHorizontalTo(speed, xCoord)
        self.headVerticalTo(speed, yCoord)

    # Move os eixos vertical e horizontal dos olhos para uma coordenada definida pelo usuário
    def eyesTo2D(self, speed, xCoord, yCoord):
        self.eyeHorizontalTo(speed, xCoord)
        self.eyeVerticalTo(speed, yCoord)


class RightArm(Servomotors):

    index_finger_GPIO_PIN = 5
    index_finger_lastPosition = 0
    index_finger_MIN_ANGLE = 40
    index_finger_MIDDLE_ANGLE = 80
    index_finger_MAX_ANGLE = 120

    def __init__(self):
        super().__init__()

    def moveTo(self, servomotor, angle, speed):
        return super().moveTo(servomotor, angle, speed)

    def fingerClose(self, speed):
        self.moveTo(self.index_finger_GPIO_PIN, self.index_finger_MAX_ANGLE, speed)
