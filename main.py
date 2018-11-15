# from packages.speech import SpeechModule
#
# output = SpeechModule()
#
# output.speak("This is a speaking test. How good am I speaking?")

from packages.servomotors import Servomotors

servo = Servomotors()
print(servo.angleToPulse(90))
servo.headUp()
