import random

from flask import Flask, Response
from flask_cors import CORS, cross_origin
from flask import request
from transformers import pipeline

import QA_model
import text_to_speech

app = Flask(__name__)
# cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'
# load model into kernel
question_answerer_model = pipeline('question-answering')
general_question_model = pipeline('fill-mask', model='bert-base-uncased')


@app.route('/profile', methods=['POST', 'GET'])
@cross_origin()
def my_profile():
    questionText = request.args.get('questionText')
    questionAudio = request.args.get('questionAudio')

    # question answering
    res = QA_model.answer(questionText, question_answerer_model, general_question_model)
    # text to audio
    transcript = res
    voice_file = "voice/raw_speech.mp3"
    modified_voice_file = "voice/modified_pitch_speech.mp3"

    # random spectrum for voice settings
    low_pitch = -0.5
    high_pitch = 0.3
    accent = random.choice(list(text_to_speech.LocalAccent))
    octave = random.uniform(low_pitch, high_pitch)

    text_to_speech.convert_text_to_audio_file(transcript, accent, voice_file)
    text_to_speech.play_voice_from_file(voice_file)

    text_to_speech.change_pitch(octave, voice_file, modified_voice_file)
    text_to_speech.play_voice_from_file(modified_voice_file)

    response_body = {
        "questionText": res,
        "questionAudio": questionAudio,
    }

    return response_body
