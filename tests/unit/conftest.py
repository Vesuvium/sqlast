# -*- coding: utf-8 -*-
from pytest import fixture


@fixture
def magic(mocker):
    """
    Shorthand for mocker.MagicMock. It's magic!
    """
    return mocker.MagicMock


@fixture
def patch_init(mocker):
    """
    Makes patching a class' constructor slightly easier
    """
    def patch_init(item):
        mocker.patch.object(item, '__init__', return_value=None)
    return patch_init


@fixture
def patch_many(mocker):
    """
    Makes patching many attributes of the same object simpler
    """
    def patch_many(item, attributes):
        for attribute in attributes:
            mocker.patch.object(item, attribute)
    return patch_many


@fixture
def patch(mocker, patch_init, patch_many):
    mocker.patch.init = patch_init
    mocker.patch.many = patch_many
    return mocker.patch


@fixture
def call_count():
    """
    Makes asserting a call count on the same module less repetitive.
    """
    def call_count(module, methods, count=1):
        for method in methods:
            assert getattr(module, method).call_count == count
    return call_count
