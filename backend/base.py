import random

from flask import Flask, Response
from flask_cors import CORS, cross_origin
from flask import request

import QA_model
import text_to_speech

app = Flask(__name__)
# cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/profile', methods = ['POST', 'GET'])
@cross_origin()
def my_profile():
    questionText = request.args.get('questionText')
    questionAudio = request.args.get('questionAudio')
    # question answering
    res = QA_model.answer(questionText)
    # text to audio
    voice_file = "voice/voice_output.mp3"
    text_to_speech.synthesize_text(res, voice_file)
    text_to_speech.play_voice_from_file(voice_file)

    response_body = {
        "questionText": res,
        "questionAudio": questionAudio,
    }

    return response_body
