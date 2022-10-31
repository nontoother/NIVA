import random
from enum import Enum
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

RATE_UPPER = 200
RATE_LOWER = 150


class VoiceGender(Enum):
    MAN = 0
    WOMAN = 1


# Set the octave which determine the audio will be thicker or thinner, value can be [-1,1]
def change_pitch_from_file(audio_file, octaves):
    sound = AudioSegment.from_file(audio_file, format="wav")
    sample_rate = int(sound.frame_rate * (2.0 ** octaves))

    # Sample rate is changed and audio become very weird. So, to fix this:
    temp_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
    # Now, For converting sample rate to standard audio CD sample rate, which is 44.1K:
    pitch_sound = temp_sound.set_frame_rate(44100)
    pitch_sound.export(audio_file, format="wav")


def play_sound_from_file(audio_file):
    play_sound = AudioSegment.from_wav(audio_file)
    play(play_sound)  # pip install simpleaudio


def generate_random_voice_settings():
    gender_list = [VoiceGender.MAN, VoiceGender.WOMAN]
    gender = random.choice(gender_list)
    rate = random.randint(RATE_LOWER, RATE_UPPER)
    octaves = random.uniform(-1.0, 1.0)
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
