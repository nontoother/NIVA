
import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment


def speech_to_text_converter():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = recognizer.listen(source2)

            # Using google to recognize audio
            text_message = recognizer.recognize_google(audio2)
            text_message = text_message.lower()

            return text_message

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")


def text_to_speech_converter(text_message):
    engine = pyttsx3.init()
    engine.say(text_message)
    engine.runAndWait()


def save_voice_to_file(text_message, file_name):
    engine = pyttsx3.init()
    engine.save_to_file(text_message, file_name)
    engine.runAndWait()


def change_voice_type():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


def change_speech_rate(): # Integer speech rate in words per minute
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')

    for index in range(5):
        engine.setProperty('rate', rate + index * 20)
        engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


def change_volume(): # Floating point volume of speech in the range [0.0, 1.0]
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')

    for index in range(5):
        engine.setProperty('volume', volume - index * 0.1)
        engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


# https://batulaiko.medium.com/how-to-pitch-shift-in-python-c59b53a84b6d
def change_pitch(octaves):  # Set the octave which determine the audio will be thicker or thinner, value can be [-1,1]
    filename = 'input.wav'
    sound = AudioSegment.from_file(filename, format="wav")
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

    # Sample rate is changed and audio become very weird. So, to fix this:
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

    # Now, For converting sample rate to standard audio CD sample rate, which is 44.1K:
    hipitch_sound = hipitch_sound.set_frame_rate(44100)

    # export / save pitch changed sound audio file via pydub
    hipitch_sound.export(f"octave_{octaves}.wav", format="wav")


