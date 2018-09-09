# -*- coding: utf-8 -*-
import click

from .App import SqlAst


class Cli:

    @click.group()
    def main():
        pass

    @staticmethod
    @main.command()
    @click.argument('path')
    def parse(path):
        click.echo(SqlAst.parse(path))
