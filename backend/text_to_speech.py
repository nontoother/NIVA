from pydub.playback import play
from pydub import AudioSegment
from google.cloud import texttospeech
import os

def play_voice_from_file(audio_file):
    sound = AudioSegment.from_mp3(audio_file)
    play(sound) 

def synthesize_text(text, voice_file):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'context/client_service_key.json'
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    # https://cloud.google.com/text-to-speech/docs/voices
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
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









