#! /usr/bin/env python
# coding: utf-8

"""apigoogle module tests, use pytest."""

import grandpyapp.utils.apigoogle as script
import config

# excepted values
data_excepted = config.API_GOOGLE_DATA_TEST


class MockRequestsGet:
    """Parent class use for monkeypatch."""

    def __init__(self, url, params=None):
        self.status_code = 200

    def json(self):
        """the json with the expected values."""
        return config.API_GOOGLE_JSON_FOR_TEST


def test_get_data_from_request_ok(monkeypatch):
    """checks if the values ​​returned are those expected."""

    class MockRequestsGetOk(MockRequestsGet):
        """mock for correct values ​​returned."""

        def __init__(self, url, params=None):
            MockRequestsGet.__init__(self, url, params)

    monkeypatch.setattr('requests.get', MockRequestsGetOk)

    response_google = script.ApiGoogle("test")
    assert response_google.get_data_from_request() == data_excepted


def test_get_data_from_request_error_values(monkeypatch):
    """check if all values ​​are returned."""

    class MockRequestsGetBadValues(MockRequestsGet):
        """mock for missing values."""

        def __init__(self, url, params=None):
            MockRequestsGet.__init__(self, url, params)

        def json(self):
            """reformulates the json with a missing value."""
            return {
                "results": [
                    {
                        "geometry": {
                            "location": {
                                # missing lat
                                "lng": data_excepted[1]
                            }
                        },
                        "place_id": data_excepted[0],
                    }
                ]
            }
    monkeypatch.setattr('requests.get', MockRequestsGetBadValues)

    response_google = script.ApiGoogle("test")
    assert response_google.get_data_from_request(
    ) == config.APP_ERROR['api_google_bad_return']


def test_get_data_from_request_ko(monkeypatch):
    """check if good error value returned if the status returned by the API is
    not 200."""

    class MockRequestsGetBadValues(MockRequestsGet):
        """mock for missing values."""

        def __init__(self, url, params=None):
            MockRequestsGet.__init__(self, url, params)
            self.status_code = 404  # bad return

    monkeypatch.setattr('requests.get', MockRequestsGetBadValues)

    response_google = script.ApiGoogle("test")
    assert response_google.get_data_from_request(
    ) == config.APP_ERROR['api_google_ko']
