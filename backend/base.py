from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from backend import QA_model

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
    
    response_body = {
        "questionText": res,
        "questionAudio": questionAudio,
    }

    return response_body

