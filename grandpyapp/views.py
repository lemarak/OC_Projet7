"""
The views and routes of the flask application
"""

from flask import Flask, render_template, jsonify, request

import json

from .utils.parserquery import ParserQuery
from .utils.apigoogle import ApiGoogle

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    """ route for index """
    return render_template('index.html')


@app.route('/query', methods=["POST"])
def query_to_grandpy():
    response = request.form["query-text-form"]
    parser_query = ParserQuery(response)
    parser_query.clean_text()
    response_google = ApiGoogle(parser_query.text_parsed)
    return jsonify(
        [parser_query.text_parsed,
         response_google.get_data_from_request()]
    )
