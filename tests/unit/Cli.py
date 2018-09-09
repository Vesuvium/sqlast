# -*- coding: utf-8 -*-
import click
from click.testing import CliRunner

from pytest import fixture

from sqlast.App import SqlAst
from sqlast.Cli import Cli


@fixture
def runner():
    return CliRunner()


def test_cli_parse(patch, runner):
    patch.object(click, 'echo')
    patch.object(SqlAst, 'parse')
    result = runner.invoke(Cli.parse, ['path'])
    SqlAst.parse.assert_called_with('path')
    click.echo.assert_called_with(SqlAst.parse())
    assert result.exit_code == 0
