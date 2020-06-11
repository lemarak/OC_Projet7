"""The views and routes of the flask application."""

import json

from flask import Flask, render_template, jsonify, request

from .utils.parseruserquery import ParserQuery
from .utils.apigoogle import ApiGoogle
from .utils.apimediawiki import ApiMediaWiki

app = Flask(__name__)

app.config.from_object("config")


@app.route("/")
@app.route("/index/")
def index():
    """route for index."""
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query_to_grandpy():
    """ """
    response = request.form["query-text-form"]
    parser_query = ParserQuery(response)
    parser_query.clean_text()
    response_google = ApiGoogle(parser_query.text_parsed)
    reponse_google_for_template = response_google.get_data_from_request()
    if reponse_google_for_template == 0:
        reponse_google_for_template = (-1, 0, 0)
        response_wiki_for_template = (
            ApiMediaWiki.get_random_text_not_found(), "#")
    else:
        response_wiki = ApiMediaWiki(parser_query.text_parsed)
        response_wiki_for_template = response_wiki.get_data_from_wiki()
    return jsonify(
        [
            parser_query.text_parsed,
            reponse_google_for_template,
            response_wiki_for_template
        ]
    )
