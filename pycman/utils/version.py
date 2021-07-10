import importlib
import os
import re
import sys

from pycman.utils import print_logo


def get_version() -> str:
    context = os.path.abspath(os.getcwd())
    sys.path.append(context)
    package = importlib.import_module('package')
    return package.package['version']


def show_version():
    print_logo()
    print("")
    print(f"version: {get_version()}")


def mark_version(version: str = None) -> str:
    """标定版本号

    Keyword Arguments:
        version {str} -- 版本号 (default: {None})
    """

    if not version:
        print('Current version: %s' % get_version())
        version = input('Please enter a new version number: v')

    is_version_legal = re.match(r'[0-9]+\.[0-9]+\.[0-9]+$', version)
    if is_version_legal:
        write_version_into_files(version)
        commit_and_tag(version)
        return version
    else:
        print(r'Please enter a valid version number [0-9]+\.[0-9]+\.[0-9]+$')
        return None


def write_version_into_files(version: str, context: str = os.getcwd()):
    # 再找到 package.py 中的 version描述
    with open(os.path.join(context, 'package.py'), encoding="utf-8") as f:
        dicts = f.read()
        dicts = re.sub(r'[0-9]+\.[0-9]+\.[0-9]+', version, dicts)

    with open(os.path.join(context, 'package.py'), 'w', encoding="utf-8") as f:
        f.write(dicts)


def commit_and_tag(version: str):
    """
    提交代码
    """
    os.system("git add .")
    os.system('git commit -m "[release] %s"' % version)
    os.system('git tag v%s' % version)
