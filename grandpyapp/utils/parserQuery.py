#! /usr/bin/env python
# coding: utf-8

"""
Parse the question asked by the user in order
to retrieve only the place requested.
"""

import json
import codecs
import re

import slugify


class ParserQuery:
    """
        1. tout transformer en minuscules
        2. éliminer les accents
        3. extraire la question
        4. éliminer les stop words
    """

    # TODO: mettre en json
    QUERY_TO_DELETE = [
        'ou se trouve',
        'ou est',
        'je veux aller',
        'parle moi de',
        'comment aller',
        'dis moi tout sur',
        'pourrais tu m indiquer',
        'est ce que tu pourrais m indiquer'
    ]

    # TODO: mettre en json
    OTHER_WORDS = [
        'grandpy',
        'grand py',
        'bonjour',
        'bonsoir',
        'salut',
        'hello',
        'salutations',
        'à bientôt',
        'trouve',
        's il te plait',
        'merci',
        'indiquer',
        'adresse',
        'mamie',
        'avance',
        'papy',
        'papi'
    ]
    PATH_JSON = 'grandpyapp/static/resources/fr.json'

    def __init__(self, text_to_parse):
        self.text_to_parse = text_to_parse
        self.text_parsed = ''

    def clean_text(self):
        """
        Chain function calls to clean up text
        """
        self.text_to_parse = self.text_to_parse.lower()
        self.text_to_parse = self.slugify_text(self.text_to_parse)
        self.delete_expression(self.QUERY_TO_DELETE, True)
        self.delete_expression(self.OTHER_WORDS)
        self.delete_words()
        self.text_parsed = self.text_to_parse

    # @staticmethod
    # def strip_accents(text_with_accents):
    #     return ''.join(c for c in unicodedata.normalize('NFD',
    #                                                     text_with_accents)
    #                    if unicodedata.category(c) != 'Mn')

    def delete_expression(self, list_expressions, before=False):
        """
        delete words or expression from a list
        if before == True : delete all words before the expression
        and the expression
        """
        for expression in list_expressions:
            if before:
                if expression in self.text_to_parse:
                    self.text_to_parse = self.text_to_parse.split(
                        expression)[-1]
            else:
                self.text_to_parse = re.sub(
                    r"(\s" + self.slugify_text(expression) + "\s)",
                    r" ",
                    self.text_to_parse)

    @staticmethod
    def slugify_text(text_to_slugify):
        """
        delete accents, specials characters
        """
        text_to_slugify = slugify.slugify(text_to_slugify)
        return text_to_slugify.replace('-', ' ')

    def delete_words(self):
        """
        open the json list and call delete expression
        """
        with codecs.open(self.PATH_JSON, 'r', 'utf-8-sig') as words_json:
            json_dict = json.load(words_json)
            self.delete_expression(json_dict)
