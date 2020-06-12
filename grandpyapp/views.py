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
    """route for index."""
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query_to_grandpy():
    """"""
    response = request.form["query-text-form"]
    parser_query = ParserQuery(response)
    parser_query.clean_text()
    api_google = ApiGoogle(parser_query.text_parsed)
    reponse_google = api_google.get_data_from_request()
    if reponse_google == 0:
        reponse_google = (-1, 0, 0)
        response_wiki = (
            ApiMediaWiki.get_random_text_not_found(), "#")
    else:
        api_wiki = ApiMediaWiki(parser_query.text_parsed)
        response_wiki = api_wiki.get_data_from_wiki()
    return jsonify(
        [
            parser_query.text_parsed,
            reponse_google,
            response_wiki
        ]
    )
