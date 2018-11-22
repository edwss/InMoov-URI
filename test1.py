from packages.servomotors import Servomotors


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