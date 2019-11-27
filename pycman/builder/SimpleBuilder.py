import os
import textwrap

from pycman.builder import BaseBuilder, InitError, utils

CONTEXT = os.path.abspath(os.getcwd())


class Builder(BaseBuilder):


    def building(self):
        utils.init_package_module(self)
        utils.init_pbr(self)
        utils.init_requirements(self)
