#! /usr/bin/env python
# coding: utf-8

"""Parse the question asked by the user in order to retrieve only the place
requested."""

import json
import codecs
import re

import slugify
import config


class ParserQuery:
    """
        1. tout transformer en minuscules
        2. éliminer les accents
        3. extraire la question
        4. éliminer les stop words
    """

    PATH_JSON = "grandpyapp/static/resources/fr.json"

    def __init__(self, text_to_parse):
        self.text_to_parse = text_to_parse
        self.text_parsed = ""

    def clean_text(self):
        """Chain function calls to clean up text."""
        self.text_to_parse = self.text_to_parse.lower()
        self.text_to_parse = self._slugify_text(self.text_to_parse)
        self._delete_expression(config.QUERY_TO_DELETE, True)
        self._delete_words()
        self.text_parsed = self.text_to_parse

    @staticmethod
    def _slugify_text(text_to_slugify):
        """delete accents, specials characters."""
        text_to_slugify = slugify.slugify(text_to_slugify)
        return text_to_slugify.replace("-", " ")

    def _delete_expression(self, list_expressions, before=False):
        """
        delete words or expression from a list
        if before == True : delete the expression and all words before this one
        """
        for expression in list_expressions:
            if before:
                if expression in self.text_to_parse:
                    self.text_to_parse = self.text_to_parse.split(expression)[
                        -1
                    ][1:]
            else:
                self.text_to_parse = " {} ".format(self.text_to_parse)
                self.text_to_parse = re.sub(
                    r"(\s" + self._slugify_text(expression) + "\s)",
                    r" ",
                    self.text_to_parse,
                )
                self.text_to_parse = self.text_to_parse.strip()

    def _delete_words(self):
        """open the json list and call delete expression."""
        json_dict = self._read_json()
        self._delete_expression(json_dict)

    def _read_json(self):
        """read the json file."""
        with codecs.open(self.PATH_JSON, "r", "utf-8-sig") as words_json:
            return json.load(words_json)
