# -*- coding: utf-8 -*-
import os

from lark import Lark

from .Grammar import Grammar
from .Indenter import CustomIndenter
from .Transformer import Transformer


class Parser:
    def __init__(self, algo='lalr', ebnf_file=None):
        self.algo = algo
        self.ebnf_file = ebnf_file

    @staticmethod
    def indenter():
        """
        Initialize the indenter
        """
        return CustomIndenter()

    @staticmethod
    def transformer():
        """
        Initialize the transformer
        """
        return Transformer()

    @staticmethod
    def default_ebnf():
        folder = os.path.dirname(__file__)
        path = os.path.join(folder, '..', 'grammar', 'grammar.ebnf')
        return os.path.realpath(path)

    def lark(self):
        if self.ebnf_file is None:
            self.ebnf_file = self.default_ebnf()
        grammar = Grammar.grammar(self.ebnf_file)
        return Lark(grammar, parser=self.algo, postlex=self.indenter())

    def parse(self, source):
        source = '{}\n'.format(source)
        lark = self.lark()
        tree = lark.parse(source)
        return self.transformer().transform(tree)
