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
        return 1

    def build(self, initializer: PycmanInitializer) -> None:
        """
        创建setup.py 及 setup.cfg
        """
        print(' -> create pbr files...')
        pbr_cfg = PBR_CONFIG % (initializer.name, initializer.author, initializer.email, initializer.name)

        with open(os.path.join(initializer.context, 'setup.cfg'), 'w', encoding="utf-8") as cfg:
            cfg.write(pbr_cfg)

        with open(os.path.join(initializer.context, 'setup.py'), 'w', encoding="utf-8") as cfg:
            cfg.write(SETUP_SCRIPT)
