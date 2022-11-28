import random

from flask import Flask, Response
from flask_cors import CORS, cross_origin
from flask import request

import QA_model
import text_to_speech
from transformers import pipeline


app = Flask(__name__)
# cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# load model into kernel
question_answerer_model = pipeline('question-answering')
general_question_model = pipeline('fill-mask', model='bert-base-uncased')

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/profile', methods = ['POST', 'GET'])
@cross_origin()
def my_profile():
    questionText = request.args.get('questionText')
    # question answering
    res = QA_model.answer(questionText, question_answerer_model, general_question_model)

    # text to audio
    raw_voice_file = "voice/voice_output.mp3"
    modified_voice_file = "voice/modified_voice_output.mp3"

    gender = random.randint(0, 1)  # 0 is female and 1 is male
    text_to_speech.synthesize_text(res, raw_voice_file, gender)
    text_to_speech.change_pitch(raw_voice_file, modified_voice_file, gender)
    text_to_speech.play_voice_from_file(modified_voice_file)

    response_body = {
        "questionText": res,
    }

    return response_body
