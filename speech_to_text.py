from enum import Enum

import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_speech_to_text(self, input_language="en-US"):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source:

                # the recognizer adjust the energy threshold based on the surrounding noise level
                self.recognizer.adjust_for_ambient_noise(source, duration=0.1)

                # listens for the user's input
                audio = self.recognizer.listen(source, timeout=3)

                # using google to recognize audio, support multi-languages
                text = self.recognizer.recognize_google(audio, language=input_language)
                return text.lower()

        except sr.UnknownValueError:
            print("Cannot convert to text")

        except sr.WaitTimeoutError:
            pass


if __name__ == "__main__":
    stt = SpeechToText()
    text_script = stt.convert_speech_to_text()
    print(text_script)



