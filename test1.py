from packages.servomotors import Servomotors
import time

servo = Servomotors()
time.sleep(2)

servo.headUp(0.5)
time.sleep(2)
servo.neutral()
time.sleep(2)

servo.headDown(0.5)
time.sleep(2)
servo.neutral()
time.sleep(2)

servo.headRight(0.5)
time.sleep(2)
servo.neutral()
time.sleep(2)

servo.headLeft(0.5)
time.sleep(2)
servo.neutral()
time.sleep(2)
