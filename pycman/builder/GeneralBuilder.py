from pycman.builder import BaseBuilder, InitError
import os
import textwrap
from pycman.builder import utils

CONTEXT = os.path.abspath(os.getcwd())


class Builder(BaseBuilder):

    def init(self):
        super().init()
        self.in_place = False
        os.mkdir(self.name)
        utils.init_meta_data(self)

    def building(self):
        utils.init_meta_data(self)
        utils.init_requirements(self)
        utils.init_project_manager(self)
        utils.init_venv(self)
        utils.init_git(self)
        utils.init_pbr(self)
        utils.init_readme(self)
