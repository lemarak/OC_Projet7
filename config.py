"""
    Constantes use by GrandPy
"""


URL_GOOGLE = "https://maps.googleapis.com/maps/api/geocode/json"
KEY_GOOGLE = "AIzaSyBUje5gmYclFjlj9V2p10HozyrDE-q4Qfw"

URL_MEDIA_WIKI = "https://fr.wikipedia.org/w/api.php"

PARAM_MEDIA_WIKI_SEARCH = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srprop": "sectiontitle|snippet"
}


PARAM_MEDIA_WIKI_PAGE = {
    "action": "query",
    "prop": "extracts",
    "explaintext": 1,
    "format": "json",
    "formatversion": 2,
    "exlimit": 1
}

QUERY_TO_DELETE = [
    'ou se trouve',
    'ou est',
    'je veux aller',
    'parle moi de',
    'comment aller',
    'dis moi tout sur',
    'pourrais tu m indiquer',
    'est ce que tu pourrais m indiquer',
    'je cherche',
    'je dois aller',
    'comment est',
    'connais tu'
]
