import importlib
import json
import os
import re
import sys

from pycman.utils import get_version, goto, import_module

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def mark_version(version: str = None):
    """标定版本号

    Keyword Arguments:
        version {str} -- 版本号 (default: {None})
    """

    if not version:
        print('Current version: %s' % get_version())
        version = input('Please enter a new version number: v')

    is_sync = input('Push to your remote? (press enter to skip) [y/n]')
    sync_flag = False
    if is_sync in ['y', 'n']:
        if is_sync == 'y':
            sync_flag = True
    if not sync_flag:
        print('About to skip the push step...')

    is_version_legal = re.match(r'[0-9]+\.[0-9]+\.[0-9]+$', version)
    if is_version_legal:
        write_version_into_files(version)
        commit(version, sync_flag)
    else:
        print(r'Please enter a valid version number [0-9]+\.[0-9]+\.[0-9]+$')


def write_version_into_files(version: str, context: str = os.getcwd()):
    # 先找到 __init__.py 中的 __version__ 描述
    package = import_module(module='package', cwd=context)
    package_name = package.package['name']

    # 找到 package 下的 __init__.py
    code = ''
    with open(os.path.join(context, package_name, '__init__.py'), encoding="utf-8") as f:
        code = f.read()
        code = re.sub(r'[0-9]+\.[0-9]+\.[0-9]+', version, code)

    with open(os.path.join(context, package_name, '__init__.py'), 'w', encoding="utf-8") as f:
        f.write(code)

    dicts = ''
    # 再找到 package.py 中的 version描述
    with open(os.path.join(context, 'package.py'), encoding="utf-8") as f:
        dicts = f.read()
        dicts = re.sub(r'[0-9]+\.[0-9]+\.[0-9]+', version, dicts)

    with open(os.path.join(context, 'package.py'), 'w', encoding="utf-8") as f:
        f.write(dicts)


def commit(version: str, sync: str):
    """
    提交代码
    """
    os.system("git add .")
    os.system('git commit -m "[release] %s"' % version)
    os.system('git tag v%s' % version)
    if sync:
        os.system('git push origin v%s' % version)
