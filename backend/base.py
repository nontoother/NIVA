from flask import Flask
from flask_cors import CORS, cross_origin
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def my_profile():
    # response = jsonify({"name": '123', "about": "shipped"})
    # response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add('Access-Control-Allow-Headers', "*")
    # response.headers.add('Access-Control-Allow-Methods', "*")

    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    # return response
    return response

