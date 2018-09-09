# -*- coding: utf-8 -*-
from lark.indenter import Indenter

from sqlast.Indenter import CustomIndenter


def test_indenter_customindenter():
    assert issubclass(CustomIndenter, Indenter)
    assert CustomIndenter.NL_type == '_NL'
    assert CustomIndenter.OPEN_PAREN_types == []
    assert CustomIndenter.CLOSE_PAREN_types == []
    assert CustomIndenter.INDENT_type == '_INDENT'
    assert CustomIndenter.DEDENT_type == '_DEDENT'
    assert CustomIndenter.tab_len == 8
