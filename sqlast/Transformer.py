# -*- coding: utf-8 -*-
from lark import Transformer as LarkTransformer

from .Tree import Tree


class Transformer(LarkTransformer):

    def __getattr__(self, attribute, *args):
        return lambda matches: Tree(attribute, matches)
