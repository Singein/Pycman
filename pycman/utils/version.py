from pycman.utils import print_logo
import importlib
import os
import sys
# 动态导入，避免重复冲突
version = importlib.import_module('pycman').__version__


def get_version(self: bool = True) -> str:
    if self:
        return version
    context = os.path.abspath(os.getcwd())
    package = importlib.import_module('package')
    return package.package['version']


def show_version():
    print_logo()
    print("")
    print(f"version: {version}")
