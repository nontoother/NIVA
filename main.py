import time

from command import process_query
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech, generate_random_voice_settings, change_pitch_from_file, play_sound_from_file

if __name__ == "__main__":

    file_name = "response_voice.wav"

    tts = TextToSpeech()
    stt = SpeechToText()

    stt.convert_speech_to_text_in_background()

    while True:
        if stt.text_script is not None:
            print(stt.text_script)
            response_script = process_query(stt.text_script)
            stt.text_script = None

            if response_script is not None:
                voice_parameter = generate_random_voice_settings()
                print(voice_parameter)
                gender = voice_parameter[0]
                rate = voice_parameter[1]
                octaves = voice_parameter[2]

                # basic settings (gender, rate, volume)
                tts.select_voice_gender(gender)
                tts.set_speech_rate(rate)
                tts.set_speech_volume(1.0)
                tts.save_voice_to_file(response_script, file_name)  # need to save to file in order to change pitch

                change_pitch_from_file(file_name, octaves)  # change pitch
                play_sound_from_file(file_name)

        time.sleep(0)
