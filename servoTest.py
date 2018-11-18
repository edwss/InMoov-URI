from packages.servomotors import Servomotors

#import time
servo = Servomotors()
print("Ok...trying head up...")
servo.headUp(0.05)
print("Ok...trying head down...")
servo.headDown(0.05)
print("Ok...trying head neutral...")
servo.neutral(0.05)
print("Ok...trying head left...")
servo.headLeft(0.05)
print("Ok...trying head right...")
servo.headRight(0.05)
print("Ok...trying head neutral...")
servo.neutral(0.05)
print("End of the test! Success!")


# while True:
#     x = int(input("Type the desired angle or -1 to close: "))
#     s = int(input("Type the servomotor from 0 to 4 or -1 to close: "))
#     if x == -1:
#         break
#
#     servo.moveTo(s, x)
#     print("Servo ", s, "moved to ", x, "...")

#servo.neutral()
