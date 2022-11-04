from flask import Flask
from flask_cors import CORS, cross_origin
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for

app = Flask(__name__)
# cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/profile', methods = ['POST', 'GET'])
@cross_origin()
def my_profile():
    questionText = request.args.get('questionText')
    questionAudio = request.args.get('questionAudio')
    
    response_body = {
        "questionText": questionText,
        "questionAudio": questionAudio,
    }

    return response_body

