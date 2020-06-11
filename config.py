"""
    Constantes use by GrandPy
"""

import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


URL_GOOGLE = "https://maps.googleapis.com/maps/api/geocode/json"

KEY_GOOGLE = os.getenv("KEY_GOOGLE")

URL_MEDIA_WIKI = "https://fr.wikipedia.org/w/api.php"

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
