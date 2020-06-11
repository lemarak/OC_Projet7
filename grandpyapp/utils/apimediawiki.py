import requests
import random

import config


class ApiMediaWiki:

    URL_API_MEDIAWIKI = config.URL_MEDIA_WIKI
    PARAM_SEARCH = config.PARAM_MEDIA_WIKI_SEARCH
    PARAM_PAGE = config.PARAM_MEDIA_WIKI_PAGE
    TEXT_RANDOM = [
        'Cet endroit ne me dis rien du tout, tu es sûr de ta question ?',
        'Je ne connais pas du tout ce lieu...',
        'COMMENT ???'
    ]

    def __init__(self, place_to_find):
        self.place = place_to_find

    def get_data_from_wiki(self):
        """   """
        list_searchs = self.get_data_from_search()
        if list_searchs == -1:
            return random.choice(self.TEXT_RANDOM), "#"
        page_id = list_searchs[0]["pageid"]
        title = list_searchs[0]["title"]
        content_page = self.get_data_from_page(page_id)
        url_link_wiki = self.get_url_wiki(title)
        return content_page, url_link_wiki

    def get_data_from_search(self):

        try:
            params = self.PARAM_SEARCH
            params["srsearch"] = self.place
            res = requests.get(url=self.URL_API_MEDIAWIKI, params=params)
            response = res.json()

            list_searchs = response["query"]["search"]

            return list_searchs

        except requests.exceptions.RequestException as e:
            return -1

    def get_data_from_page(self, page_id):
        try:
            params = self.PARAM_PAGE
            params["pageids"] = page_id
            res = requests.get(url=self.URL_API_MEDIAWIKI, params=params)
            response = res.json()

            return response["query"]["pages"][0]["extract"]

        except requests.exceptions.RequestException as e:
            return -1

    def get_url_wiki(self, title):
        url = "https://fr.wikipedia.org/wiki/{}".format(
            title.replace(" ", "_"))
        print(url)
        return url

    @classmethod
    def get_random_text_not_found(cls):
        return random.choice(cls.TEXT_RANDOM)
