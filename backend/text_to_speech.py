from pydub.playback import play
from pydub import AudioSegment
from google.cloud import texttospeech
import os
import random

voice_list = [
    # male's voice
    "en-US-Neural2-A",
    "en-US-Neural2-D",
    "en-US-Neural2-I",
    "en-US-Neural2-J",
    "en-US-News-M",
    "en-US-News-N",
    "en-US-Standard-A",
    "en-US-Standard-B",
    "en-US-Standard-D",
    "en-US-Standard-I",
    "en-US-Standard-J",
    "en-US-Wavenet-A",
    "en-US-Wavenet-B",
    "en-US-Wavenet-D",
    "en-US-Wavenet-I",
    "en-US-Wavenet-J",

    # female's voice
    "en-US-Neural2-C",
    "en-US-Neural2-E",
    "en-US-Neural2-F",
    "en-US-Neural2-G",
    "en-US-Neural2-H",
    "en-US-News-K",
    "en-US-News-L",
    "en-US-Standard-C",
    "en-US-Standard-E",
    "en-US-Standard-F",
    "en-US-Standard-G",
    "en-US-Standard-H",
    "en-US-Wavenet-C",
    "en-US-Wavenet-E",
    "en-US-Wavenet-F",
    "en-US-Wavenet-G",
    "en-US-Wavenet-H"]


def play_voice_from_file(audio_file):
    sound = AudioSegment.from_mp3(audio_file)
    play(sound)


def synthesize_text(text, voice_file):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../client_service_key.json'
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)
    voice_name = random.choice(voice_list)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    # https://cloud.google.com/text-to-speech/docs/voices
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name=voice_name,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=0,
        pitch=0,
        volume_gain_db=0,
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(voice_file, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
