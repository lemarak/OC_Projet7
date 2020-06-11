"""API Request google geocoding."""

import requests

import config


class ApiGoogle:

    URL_API_GEOCODING = config.URL_GOOGLE
    KEY_GOOGLE = config.KEY_GOOGLE

    def __init__(self, place):
        self.place = place

    @property
    def url_geocoding(self):
        url = "{}?address={}&key={}".format(
            self.URL_API_GEOCODING,
            self.place.replace(" ", "+"),
            self.KEY_GOOGLE,
        )
        return url

    def get_data_from_request(self):
        try:
            res = requests.get(self.url_geocoding)
            response = res.json()
            if response["status"] == "OK":
                place_id = response["results"][0]["place_id"]
                lat = response["results"][0]["geometry"]["location"]["lat"]
                lng = response["results"][0]["geometry"]["location"]["lng"]
                return place_id, lat, lng

            return 0
        except requests.exceptions.RequestException as e:
            print("ERROR: {}".format(self.place))
            return -1
