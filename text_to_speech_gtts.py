
from gtts import gTTS
from pydub.playback import play
from pydub import AudioSegment

raw_audio_file = "voice.mp3"
modified_audio_file = "modified_voice.mp3"

text = "this is a test conversion for NIVA project"
top_level_domain = "co.uk"
language = 'en'

sound_obj = gTTS(text=text, tld=top_level_domain, lang=language, slow=False)
sound_obj.save(raw_audio_file)

sound = AudioSegment.from_mp3(raw_audio_file)
play(sound)  # pip install simpleaudio

octaves = -0.4
sample_rate = int(sound.frame_rate * (2.0 ** octaves))
temp_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
pitch_sound = temp_sound.set_frame_rate(44100)
pitch_sound.export(modified_audio_file, format="mp3")

sound2 = AudioSegment.from_mp3(modified_audio_file)
play(sound2)
