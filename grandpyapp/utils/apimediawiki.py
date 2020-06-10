import requests

import config


class ApiMediaWiki:

    URL_API_MEDIAWIKI = config.URL_MEDIA_WIKI
    PARAM_MEDIA_WIKI = config.PARAM_MEDIA_WIKI

    def __init__(self, place_to_find):
        self.place = place_to_find

    def get_url(self):
        params = ""
        for key, value in self.PARAM_MEDIA_WIKI.items():
            params += "{}={}&".format(key, value)
        params += "titles={}".format(self.place.replace(" ", "_"))
        url = "{}?{}".format(self.URL_API_MEDIAWIKI, params)
        print(url)
        return url

    def get_data_from_request(self):

        try:
            res = requests.get(self.get_url())
            response = res.json()
            if response['batchcomplete']:
                full_text = response['query']['pages'][0]['extract']
                extracted_text = full_text[:800]
                return extracted_text
            return "Je ne me souviens pas de {}.".format(self.place)
        except:
            print('ERROR: {}'.format(self.place))
            return "La requête mediawiki n'a pas abouti."
