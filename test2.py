from packages.servomotors import Servomotors

servo = Servomotors()

# Aponta para a aresta da origem
servo.headLeft(0.05)
servo.headDown(0.05)

# Inicia a "desenhar" o quadrado
servo.headUp(0.05)
servo.headRight(0.05)
servo.headDown(0.05)
servo.headLeft(0.05)

# Aponta para o meio-baixo
servo.neutral(0.05)
servo.headDown(0.05)

# Inicia a "desenhar" o triângulo
servo.headTo2D(0.05, servo.head_horizontal_MAX_ANGLE, servo.head_vertical_MIDDLE_ANGLE)
servo.headTo2D(0.05, servo.head_horizontal_MIDDLE_ANGLE, servo.head_vertical_MAX_ANGLE)
servo.headTo2D(0.05, servo.head_horizontal_MIN_ANGLE, servo.head_vertical_MIDDLE_ANGLE)
servo.headTo2D(0.05, servo.head_horizontal_MIDDLE_ANGLE, servo.head_vertical_MIN_ANGLE)

