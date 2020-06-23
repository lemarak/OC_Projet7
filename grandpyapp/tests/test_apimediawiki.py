#! /usr/bin/env python
# coding: utf-8

"""apimediawiki module tests, use pytest."""

import grandpyapp.utils.apimediawiki as script
import config

# excepted values from get_data_from_wiki
data_excepted_search = config.API_MEDIA_WIKI_SEARCH_FOR_TEST
data_excepted_page = config.API_MEDIA_WIKI_PAGE_FOR_TEST


class MockRequestsGet:
    """Parent class use for monkeypatch.
    Requests media wiki search"""
    # pylint: disable=too-few-public-methods

    def __init__(self, url, params=None):
        self.status_code = 200

    def json(self):
        """the json with the expected values."""
        return {}


# Tests from API Media Wiki Search
def test_get_data_from_search_ok(monkeypatch):
    """
    Test get_data_from_search
    Checks if the values ​​returned by api mediawiki search
    are those expected.
    return == data_excepted_search.
    """

    class MockRequestsGetOk(MockRequestsGet):
        """mock for correct values ​​returned."""
        # pylint: disable=too-few-public-methods

        def __init__(self, url, params=None):
            MockRequestsGet.__init__(
                self, url, params)

        def json(self):
            """the json with the expected values."""
            return config.API_MEDIA_WIKI_SEARCH_JSON

    monkeypatch.setattr('requests.get', MockRequestsGetOk)

    response_wiki = script.ApiMediaWiki("Lieu", 10.1, 20.1)
    assert response_wiki.get_data_from_search() == data_excepted_search


# Test from API Media Wiki Page
def test_get_data_from_page_ok(monkeypatch):
    """
    Test get_data_from_page
    Checks if the values ​​returned by api mediawiki page
    are those expected.
    return == data_excepted_page.
    """

    class MockRequestsGetOk(MockRequestsGet):
        """mock for correct values ​​returned."""
        # pylint: disable=too-few-public-methods

        def __init__(self, url, params=None):
            MockRequestsGet.__init__(
                self, url, params)

        def json(self):
            """the json with the expected values."""
            return config.API_MEDIA_WIKI_PAGE_JSON

    monkeypatch.setattr('requests.get', MockRequestsGetOk)

    response_wiki = script.ApiMediaWiki("Lieu", 10.1, 20.1)
    assert response_wiki.get_data_from_page(123456) == data_excepted_page


def test_url_wikipedia():
    response_wiki = script.ApiMediaWiki("Lieu", 10.1, 20.1)
    assert response_wiki.get_url_wiki(
        "lieu") == "https://fr.wikipedia.org/wiki/lieu"
