# -*- coding: utf-8 -*-
import io

from .Parser import Parser


class SqlAst:

    @staticmethod
    def parse(path):
        with io.open(path, 'r') as file:
            source = file.read()
        return Parser().parse(source)
