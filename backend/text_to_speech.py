from pydub.playback import play
from pydub import AudioSegment
from google.cloud import texttospeech
import os
import random

male_voice_list = [
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
    "en-US-Wavenet-J"]

female_voice_list=[
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


def random_select_voice(gender):
    if gender == 0:
        return random.choice(female_voice_list)
    elif gender == 1:
        return random.choice(male_voice_list)


def synthesize_text(text, voice_file, gender):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    # https://cloud.google.com/text-to-speech/docs/voices
    voice_name = random_select_voice(gender)
    print("voice_name", voice_name)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name=voice_name,
    )

    rate = 1.0
    # make slow rate for male voice since change_pitch function will increase the rate for male voice
    if gender == 1:
        rate = 0.7

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=rate,
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


def change_pitch(raw_audio_file, modified_audio_file, gender):
    octaves = 0
    if gender == 0:
        octaves = -0.25
    elif gender == 1:
        octaves = 0.35
    sound = AudioSegment.from_mp3(raw_audio_file)
    sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    sound_obj = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
    modified_sound = sound_obj.set_frame_rate(44100)
    modified_sound.export(modified_audio_file, format="mp3")

