from subprocess import call


class SpeechModule:
    lastText = ""

    def __init__(self):
        super().__init__()

    def speak(self, text):

        self.lastText = text

        cmd_beg = 'espeak -s160 '
        cmd_end = ' 2>/dev/null'

        print(text)

        text = text.replace(' ', '_')

        call([cmd_beg+text+cmd_end], shell=True)

