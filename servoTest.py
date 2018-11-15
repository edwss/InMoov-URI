from packages.servomotors import Servomotors
import time
servo = Servomotors()
print(servo.angleToPulse(90))
servo.neutral()
servo.headUp(0.5)



# while True:
#     x = int(input("Type the desired angle or -1 to close: "))
#     s = int(input("Type the servomotor from 0 to 4 or -1 to close: "))
#     if x == -1:
#         break
#
#     servo.moveTo(s, x)
#     print("Servo ", s, "moved to ", x, "...")

#servo.neutral()
