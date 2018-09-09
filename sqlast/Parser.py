# -*- coding: utf-8 -*-
from lark import Lark

from .Grammar import Grammar
from .Indenter import CustomIndenter
from .Transformer import Transformer


class Parser:
    def __init__(self, algo='lalr', ebnf_file='grammar.ebnf'):
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

    def lark(self):
        grammar = Grammar.grammar(self.ebnf_file)
        return Lark(grammar, parser=self.algo, postlex=self.indenter())

    def parse(self, source):
        source = '{}\n'.format(source)
        lark = self.lark()
        tree = lark.parse(source)
        return self.transformer().transform(tree)
