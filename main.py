import threading

from command import Command
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech


def listen():
    while True:
        print("Listening .......")
        text_script = stt.convert_speech_to_text()
        if text_script is not None:
            if "hello" in text_script:
                activate_flag.set()
                print("How can I help you")
                #tts.convert_text_to_speech("How can I help you")

            if "stop" in text_script:
                activate_flag.clear()
                print("See you next time")
                #tts.convert_text_to_speech("See you next time")


def run_NIVA():
    while activate_flag.is_set():
        pass


if __name__ == "__main__":

    tts = TextToSpeech()
    stt = SpeechToText()
    cmd = Command()

    activate_flag = threading.Event()
    activate_flag.clear()

    # thread 1 keep listening (start or stop flag)
    listening_thread = threading.Thread(target=listen, args=())

    # thread 2 handle the NIVA operation
    # todo

    listening_thread.start()
    listening_thread.join()


