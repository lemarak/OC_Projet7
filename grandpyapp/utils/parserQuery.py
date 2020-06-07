#! /usr/bin/env python
# coding: utf-8

import slugify
import json
import codecs
import re


class ParserQuery:
    """
        1. tout transformer en minuscules (ou en maj)
        2. éliminer les accents
        3. extraire la question
        4. eventuellement éliminer les stop words
    """

    # TODO: mettre en json
    EXPRESSION_TO_DELETE = [
        'grandpy',
        'grand py',
        'bonjour',
        'bonsoir',
        'salut',
        'hello',
        'salutations',
        'à bientôt',
        'ou se trouve',
        'ou est',
        'je veux aller',
        'parle moi de',
        'comment aller',
        'dis moi tout sur',
        's\'il te plait',
        'merci',
        'pourrais-tu m\'indiquer',
        'indiquer',
        'adresse'
    ]
    PATH_JSON = 'grandpyapp/static/resources/fr.json'

    def __init__(self, text_to_parse):
        self.text_to_parse = text_to_parse

    def clean_text(self):
        self.text_to_parse = self.text_to_parse.lower()
        self.text_to_parse = self.slugify_text(self.text_to_parse)
        self.delete_expression(self.EXPRESSION_TO_DELETE)
        self.delete_words()

    # @staticmethod
    # def strip_accents(text_with_accents):
    #     return ''.join(c for c in unicodedata.normalize('NFD',
    #                                                     text_with_accents)
    #                    if unicodedata.category(c) != 'Mn')

    def delete_expression(self, list_expressions):
        for expression in list_expressions:
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
        delete the words contained in the json list
        """
        with codecs.open(self.PATH_JSON, 'r', 'utf-8-sig') as words_json:
            json_dict = json.load(words_json)
            self.delete_expression(json_dict)
