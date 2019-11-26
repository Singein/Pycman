from pycman.utils import print_logo
import importlib

# 动态导入，避免重复冲突
version = importlib.import_module('pycman').__init__


def get_version():
    return version


def show_version():
    print_logo()
    print("")
    print(f"version: {version}")
