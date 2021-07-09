from __future__ import annotations

import os

from pycman.utils.common import goto
from pycman.utils.common import import_module


def test_goto():
    """

    Returns:

    """
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    with goto(parent_path):
        assert os.getcwd() == parent_path

    assert os.getcwd() == current_path


def test_builder():
    import_module()
    print(builders)


if __name__ == '__main__':
    test_builder()
    pass
