import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.text_script = None

    def callback_recognize_audio(self, recognizer, audio):
        # using google to recognize audio, support multi-languages, default is English
        try:
            transcript = recognizer.recognize_google(audio)
            self.text_script = transcript.lower()

        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            pass
        except sr.RequestError as e:
            pass

    def convert_speech_to_text_in_background(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        # use the microphone as source for input.
        with mic as source:
            # the recognizer adjust the energy threshold based on the surrounding noise level
            recognizer.adjust_for_ambient_noise(source, duration=0.1)

        # listens for the user's input
        recognizer.listen_in_background(source, self.callback_recognize_audio, phrase_time_limit=5)

