from subprocess import call


class SpeechModule:
    lastText = ""

    def __init__(self):
        super().__init__()

    def speak(self, text):

        self.lastText = text

        cmd_beg = 'espeak'
        cmd_end = ' | aplay /home/pi/Desktop/Text.wav 2>/dev/null'
        cmd_out = '--stdout > /home/pi/Desktop/Text.wav '

        print(text)

        text = text.replace(' ', '_')

        call([cmd_beg+cmd_out+text+cmd_end], shell=True)

