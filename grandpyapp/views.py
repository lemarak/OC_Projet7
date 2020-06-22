"""The views and routes of the flask application."""

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
    response = request.form["query-text-form"]
    parser_query = ParserQuery(response)
    parser_query.clean_text()
    api_google = ApiGoogle(parser_query.text_parsed)
    response_google = api_google.get_data_from_request()

    # if error
    if response_google in (-1, -2):
        response_google = (-1, 0, 0)
        response_wiki = (
            "", ApiMediaWiki.get_random_text_not_found(), "#")
    # if ok
    else:
        api_wiki = ApiMediaWiki(parser_query.text_parsed)
        response_wiki = api_wiki.get_data_from_wiki()
    return jsonify(
        [
            parser_query.text_parsed,
            response_google,
            response_wiki
        ]
    )
