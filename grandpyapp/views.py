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
    """route for index (main page)"""
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query_to_grandpy():
    """ Functions related to the query route.
        Called at each validation of the form """
    # form data (by POST)
    response = request.form["query-text-form"]
    # parse with ParserQuery Classe
    parser_query = ParserQuery(response)
    parser_query.clean_text()
    # use API Google with parsed query
    api_google = ApiGoogle(parser_query.text_parsed)
    response_google = json.loads(api_google.get_data_from_request())

    # if error
    if response_google in (-1, -2):
        response_google = {'place_id': 0, 'lat': 0, 'lng': 0}
        response_wiki = {
            'response_grandpy': "",
            'content_page': ApiMediaWiki.get_random_text_not_found(),
            'url_link_wiki': "#"
        }
    # if ok
    else:
        api_wiki = ApiMediaWiki(parser_query.text_parsed,
                                response_google['lat'],
                                response_google['lng'])
        response_wiki = json.loads(api_wiki.get_data_from_wiki())
    return jsonify(
        {
            "text_parsed": parser_query.text_parsed,
            "response_google": response_google,
            "response_wiki": response_wiki
        }
    )
