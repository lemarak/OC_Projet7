#! /usr/bin/env python
# coding: utf-8

"""API Request google geocoding."""

import requests

import config


class ApiGoogle:
    """API Request google geocoding.

    Use the google API url, the key google and the place to search
    """

    URL_API_GEOCODING = config.URL_GOOGLE
    KEY_GOOGLE = config.KEY_GOOGLE
    APP_ERROR = config.APP_ERROR

    def __init__(self, place):
        self.place = place

    @property
    def payload(self):
        """Defines the parameters of the Get request."""
        return {"address": self.place.replace(" ", "+"),
                "key": self.KEY_GOOGLE}

    def get_data_from_request(self):
        """Execute the API request and return:

        - placeid: the google place id
        - lat: latitude
        - lng: longitude
        """
        try:
            res = requests.get(self.URL_API_GEOCODING, params=self.payload)

            if res.status_code == 200:
                if res.json()['status'] == 'ZERO_RESULTS':
                    raise KeyError('nodata')
                response = res.json()["results"][0]
                place_id = response["place_id"]
                lat = response["geometry"]["location"]["lat"]
                lng = response["geometry"]["location"]["lng"]
                return place_id, lat, lng
            return self.APP_ERROR['api_google_ko']
        except requests.exceptions.RequestException:
            return self.APP_ERROR['api_google_ko']
        except KeyError:
            return self.APP_ERROR['api_google_bad_return']
