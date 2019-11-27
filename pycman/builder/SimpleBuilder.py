import os
import textwrap

from pycman.builder import BaseBuilder, InitError, utils

CONTEXT = os.path.abspath(os.getcwd())


class Builder(BaseBuilder):

    def init(self):
        super().init()
        self.in_place = True
        if not self.name in os.listdir(CONTEXT):
            os.mkdir(self.name)
            with open(os.path.join(CONTEXT, self.name, '__init__.py'), 'w', encoding="utf-8") as f:
                f.write('__version__ = "0.0.1"')


    def building(self):
        utils.init_package_module(self)
        utils.init_pbr(self)
        utils.init_requirements(self)
        utils.init_readme(self)
        utils.init_git(self)
