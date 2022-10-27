from enum import Enum
import pyttsx3


class VoiceGender(Enum):
    MAN = 0
    WOMAN = 1


class TextToSpeech:

    def __init__(self):
        self.engine = pyttsx3.init()

    def convert_text_to_speech(self, text_message):
        self.engine.say(text_message)
        self.engine.runAndWait()

    def save_voice_to_file(self, text, file_name):
        self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()

    # gender_index: either VoiceGender.MAN or VoiceGender.WOMAN
    def select_voice_gender(self, gender):
        voices = self.engine.getProperty('voices')
        voice_id = None
        if gender == VoiceGender.MAN:
            voice_id = voices[0].id
        if gender == VoiceGender.WOMAN:
            voice_id = voices[1].id
        self.engine.setProperty('voice', voice_id)
        self.engine.runAndWait()

    # integer speech rate in words per minute
    def set_speech_rate(self, speech_rate):
        self.engine.setProperty('rate', speech_rate)
        self.engine.runAndWait()

    # floating point volume of speech in the range [0.0, 1.0]
    def set_speech_volume(self, speech_volume):
        self.engine.setProperty('volume', speech_volume)
        self.engine.runAndWait()


if __name__ == "__main__":

    text_script = "This is a test for NIVA project"
    file_name = "test.wav"

    tts = TextToSpeech()
    tts.select_voice_gender(VoiceGender.WOMAN)
    tts.set_speech_rate(150)
    tts.set_speech_volume(1.0)
    tts.convert_text_to_speech(text_script)
    tts.save_voice_to_file(text_script, file_name)

    # todo: change pitch
    # https://batulaiko.medium.com/how-to-pitch-shift-in-python-c59b53a84b6d



