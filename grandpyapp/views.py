"""
The views and routes of the flask application
"""

from flask import Flask, render_template, jsonify, request
from .utils.parserQuery import ParserQuery

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    """ route for index """
    return render_template('index.html')


@app.route('/query', methods=["POST"])
def query_to_grandpy():
    response = request.form["text-query"]
    print(response)
    parser_query = ParserQuery(response)
    print(parser_query.text_to_parse_cleaned_up)
    return jsonify(["pas de réponse"])
