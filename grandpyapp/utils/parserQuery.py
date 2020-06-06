#! /usr/bin/env python
# coding: utf-8

import unicodedata


class ParserQuery:
    """
        1. tout transformer en minuscules (ou en maj)
        2. éliminer les accents
        3. extraire la question avec une expression rationnelle
        4. eventuellement éliminer les stop words (mais n'apporte pas grand chose)
    """

    EXPRESSION_TO_DELETE = [
        'ou se trouve',
        'ou est',
        'je veux aller',
        'parle moi de',
        'comment aller',
        'dis moi tout sur'
    ]

    def __init__(self, text_to_parse):
        self.text_to_parse = text_to_parse

    @property
    def text_to_parse_cleaned_up(self):
        self.text_to_parse = self.strip_accents()
        return self.text_to_parse.lower()

    def strip_accents(self):
        return ''.join(c for c in unicodedata.normalize('NFD',
                                                        self.text_to_parse)
                       if unicodedata.category(c) != 'Mn')
