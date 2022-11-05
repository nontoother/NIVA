from enum import Enum
from gtts import gTTS
from pydub.playback import play
from pydub import AudioSegment


class LocalAccent(Enum):
    AUSTRALIA = 0
    UK = 1
    US = 2
    CANADA = 3
    INDIA = 4
    IRELAND = 5
    SOUTH_AFRICA = 6


accent_dict = {
    LocalAccent.AUSTRALIA: "com.au",
    LocalAccent.UK: "co.uk",
    LocalAccent.US: "com",
    LocalAccent.CANADA: "ca",
    LocalAccent.INDIA: "co.in",
    LocalAccent.IRELAND: "ie",
    LocalAccent.SOUTH_AFRICA: "co.za"
}


def convert_text_to_audio_file(text, accent, audio_file):
    top_level_domain = accent_dict[accent]
    sound_obj = gTTS(text=text, tld=top_level_domain, lang='en', slow=False)
    sound_obj.save(audio_file)  # .mp3 format eg: "test.mp3"


def change_pitch(octaves, raw_audio_file, modified_audio_file):
    sound = AudioSegment.from_mp3(raw_audio_file)
    sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    sound_obj = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
    modified_sound = sound_obj.set_frame_rate(44100)
    modified_sound.export(modified_audio_file, format="mp3")


def play_voice_from_file(audio_file):
    sound = AudioSegment.from_mp3(audio_file)
    play(sound)  # pip install simpleaudio


if __name__ == "__main__":
    transcript = "this is a test for text to speech conversion"
    voice_file = "test.mp3"
    modified_voice_file = "modified_test.mp3"

    convert_text_to_audio_file(transcript, LocalAccent.UK, voice_file)
    play_voice_from_file(voice_file)

    change_pitch(0.5, voice_file, modified_voice_file)
    play_voice_from_file(modified_voice_file)



