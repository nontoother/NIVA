import random
from enum import Enum
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

RATE_UPPER = 200
RATE_LOWER = 150
OCTAVES_UPPER = 0.5
OCTAVES_LOWER = -0.1

# It works fully offline
# choose among different voices that are installed on your system
#https://www.thepythoncode.com/article/convert-text-to-speech-in-python

class VoiceGender(Enum):
    MAN = 0
    WOMAN = 1


# Set the octave which determine the audio will be thicker or thinner, value can be [-1,1]
def change_pitch_from_file(audio_file, octaves):
    sound = AudioSegment.from_file(audio_file, format="mp3")
    #sample_rate = int(sound.frame_rate * (2.0 ** octaves))

    # Sample rate is changed and audio become very weird. So, to fix this:
    #temp_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
    # Now, For converting sample rate to standard audio CD sample rate, which is 44.1K:
    #pitch_sound = temp_sound.set_frame_rate(44100)
    #pitch_sound.export(output_file, format="wav")


def play_sound_from_file(audio_file):
    play_sound = AudioSegment.from_mp3(audio_file)
    play(play_sound)  # pip install simpleaudio


def generate_random_voice_settings():
    gender_list = [VoiceGender.MAN, VoiceGender.WOMAN]
    gender = random.choice(gender_list)
    rate = random.randint(RATE_LOWER, RATE_UPPER)
    octaves = random.uniform(OCTAVES_LOWER, OCTAVES_UPPER)
    return [gender, rate, octaves]


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
    def select_voice_gender(self):
        voices = self.engine.getProperty('voice')
        print(voices)
# todo: instead of select gender, let it choose id based on different os platform
        # for v in voices:
        #     self.engine.setProperty('voice', v.id)
        #     self.engine.say("how are you nice to meet you")
        #     print(v.id)

        # voice_id = None
        # if gender == VoiceGender.MAN:
        #     voice_id = voices[0].id
        # if gender == VoiceGender.WOMAN:
        #     voice_id = voices[1].id
        # self.engine.setProperty('voice', voice_id)
        # self.engine.runAndWait()

    # integer speech rate in words per minute
    def set_speech_rate(self, speech_rate):
        self.engine.setProperty('rate', speech_rate)
        self.engine.runAndWait()

    # floating point volume of speech in the range [0.0, 1.0]
    def set_speech_volume(self, speech_volume):
        self.engine.setProperty('volume', speech_volume)
        self.engine.runAndWait()


if __name__ == "__main__":
    response_script = "This is a test program for NIVA design for backend"
    tts = TextToSpeech()
    tts.set_speech_rate(80)
    tts.select_voice_gender()

    #tts.convert_text_to_speech(response_script)
