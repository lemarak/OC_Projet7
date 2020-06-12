"""Constantes use by GrandPy."""

import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


URL_GOOGLE = "https://maps.googleapis.com/maps/api/geocode/json"

KEY_GOOGLE = os.getenv("KEY_GOOGLE")

URL_MEDIA_WIKI = "https://fr.wikipedia.org/w/api.php"

APP_ERROR = {
    "api_google_ko": -1,
    "api_google_bad_return": -2,
    "api_mediawiki_ko": -3,
    "api_mediawiki_bad_return": -2,
}

API_GOOGLE_DATA_TEST = ("123456", 10.1, 20.1)

API_GOOGLE_JSON_FOR_TEST = {
    "results": [
        {
            "geometry": {
                "location": {
                    "lat": API_GOOGLE_DATA_TEST[1],
                    "lng": API_GOOGLE_DATA_TEST[2]
                }
            },
            "place_id": API_GOOGLE_DATA_TEST[0],
        }
    ]
}

PARAM_MEDIA_WIKI_SEARCH = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srprop": "sectiontitle|snippet",
}

PARAM_MEDIA_WIKI_PAGE = {
    "action": "query",
    "prop": "extracts",
    "explaintext": 1,
    "format": "json",
    "formatversion": 2,
    "exlimit": 1,
    "exsentences": 5,
}

QUERY_TO_DELETE = [
    "ou se trouve",
    "ou est",
    "je veux aller",
    "parle moi de",
    "comment aller",
    "dis moi tout sur",
    "pourrais tu m indiquer",
    "est ce que tu pourrais m indiquer",
    "je cherche",
    "je dois aller",
    "comment est",
    "connais tu",
]
