# -*- coding: utf-8 -*-
import io


class Grammar:

    @staticmethod
    def grammar(ebnf_file):
        with io.open(ebnf_file) as file:
            return file.read()
