# -*- coding: utf-8 -*-
import io

from sqlast.App import SqlAst
from sqlast.Parser import Parser


def test_app_sqlast_parse(patch):
    patch.object(io, 'open')
    patch.init(Parser)
    patch.object(Parser, 'parse')
    result = SqlAst.parse('path')
    io.open.assert_called_with('path', 'r')
    Parser.parse.assert_called_with(io.open().__enter__().read())
    assert result == Parser.parse()
