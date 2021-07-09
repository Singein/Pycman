import os

from pycman.core import PycmanInitializer
from pycman.core.initializer import AbstractBuilder

PBR_CONFIG = """
[metadata]
name = %s
author = %s
author-email = %s
summary = awsome project created by pycman.
license = MIT
description-file = 
    README.rst
home-page = http://example.com
requires-python = >= 3.6

[files]
packages = 
    %s


[entry_points]
console_scripts =
    cmd=package.module:function
""".strip()

SETUP_SCRIPT = """
import setuptools
setuptools.setup(setup_requires=['pbr'], pbr=True)
""".strip()


class Builder(AbstractBuilder):
    def order(self) -> int:
        return 3

    def build(self, initializer: PycmanInitializer) -> None:
        """
        创建依赖文件
        """
        print(' -> create requirements.txt...')
        default_requirements = []
        with open(os.path.join(initializer.context, 'requirements.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(default_requirements))
