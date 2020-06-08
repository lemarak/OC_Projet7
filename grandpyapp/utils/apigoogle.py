"""
API Request google geocoding
"""
import json

import requests


class ApiGoogle:

    URL_API_GEOCODING = "https://maps.googleapis.com/maps/api/geocode/json"
    KEY_GOOGLE = ""

    def __init__(self, place):
        self.place = place

    @property
    def url_geocoding(self):
        url = ('{}?address={}&key={}'
               .format(self.URL_API_GEOCODING,
                       self.place.replace(' ', '+'),
                       self.KEY_GOOGLE))
        return url

    def get_data_from_request(self):
        try:
            res = requests.get(self.url_geocoding)
            response = res.json()
            if response['status'] == 'OK':
                return response['results'][0]['place_id']
            return "Je n'ai pas compris la question..."
        except:
            print('ERROR: {}'.format(self.place))
            return "La requête n'a pas abouti."
