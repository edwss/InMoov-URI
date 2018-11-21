from packages.servomotors import Servomotors

servo = Servomotors()

servo.mouthClose(0.05)
servo.mouthOpen(0.02)
servo.moveTo(servo.mouth_GPIO_PIN, servo.mouth_MIDDLE_ANGLE, 0.1)
servo.mouthClose(0.05)

# Always set the InMoov to the neutral position before ending your program!
servo.neutral(0.05)

