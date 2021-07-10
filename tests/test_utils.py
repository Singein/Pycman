from __future__ import annotations

import os

from pycman.core.initializer import AbstractBuilder
from pycman.utils.common import goto
from pycman.utils.common import import_module


def test_goto():
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    with goto(parent_path):
        assert os.getcwd() == parent_path

    assert os.getcwd() == current_path


def test_builder():
    builders = import_module()
    assert builders is not None

    builders = AbstractBuilder.get_builders()
    assert len(builders) >= 0
    for index in range(len(builders) - 1):
        assert builders[index] < builders[index + 1]
