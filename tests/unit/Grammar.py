# -*- coding: utf-8 -*-
import io

from sqlast.Grammar import Grammar


def test_grammar_grammar(patch):
    patch.object(io, 'open')
    result = Grammar.grammar('grammar.ebnf')
    io.open.assert_called_with('grammar.ebnf')
    assert result == io.open().__enter__().read()
