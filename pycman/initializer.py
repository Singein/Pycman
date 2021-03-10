import os
import re


class InitError(BaseException):
    pass


PACKAGE_CONTENTS = """
package = {
    'name': '%s',
    'version': '0.0.1',
    'author': '%s',
    'email': '%s',
    'scripts': {
        'default': 'echo 请输入明确的命令名称'
    }
}
""".strip()

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


class PycmanInitializer:
    def __init__(self, context: str, name: str = None, author: str = None, email: str = None):
        """
        初始化设置，这里用来初始化项目信息，
        最基本要素：项目名，作者，邮箱
        """

        if not context:
            raise InitError("self.context unknown")

        self.context = context

        if name is None:
            self.name = input('Project name: ')
            if not self.name:
                raise InitError("Project name can't be empty.")
        else:
            self.name = name

        if author is None:
            self.author = input('Author: ')
            if not self.author:
                raise InitError("Author can't be empty.")
        else:
            self.author = author

        if email is None:
            self.email = input('Email: ')
            if not self.email:
                raise InitError("Email can't be empty.")
        else:
            self.email = email

        rex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(rex, self.email):
            raise InitError("Email Invalid.")

        self.init()

    def init(self):
        from pycman.utils import print_logo
        print_logo()
        print('==> PycmanInitializer started')
        self.init_package_module()
        self.init_pbr()
        self.init_requirements()
        self.init_readme()
        self.init_git()
        print('==> All done.')

    def init_package_module(self):
        print(' -> create package.py...')
        with open(os.path.join(self.context, 'package.py'), 'w', encoding='utf-8') as f:
            f.write(PACKAGE_CONTENTS.strip() % (self.name, self.author, self.email))

    def init_pbr(self):
        print(' -> create pbr files...')
        pbr_cfg = PBR_CONFIG % (self.name, self.author, self.email, self.name)

        with open(os.path.join(self.context, 'setup.cfg'), 'w', encoding="utf-8") as cfg:
            cfg.write(pbr_cfg)

        with open(os.path.join(self.context, 'setup.py'), 'w', encoding="utf-8") as cfg:
            cfg.write(SETUP_SCRIPT)

    def init_requirements(self):
        print(' -> create requirements.txt...')
        default_requirements = []
        with open(os.path.join(self.context, 'requirements.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(default_requirements))

    def init_git(self):
        """
        请在 package_module 初始化完成后调用
        """
        if 'package.py' not in os.listdir():
            os.chdir(self.context)

        # if '.git' not in os.listdir():
        #     os.system('git init')

        if '.gitignore' not in os.listdir():
            print(' -> create .gitignore...')
            default_ignores = ['venv/', '__pycache__/',
                               '*.ini', '.eggs/', '*.egg-info', 'dist/', 'build/']
            with open(os.path.join(self.context, '.gitignore'), 'w', encoding='utf-8') as f:
                f.write('\n'.join(default_ignores))

    def init_readme(self):
        print(' -> create readme docs...')
        if not os.path.exists(os.path.join(self.context, 'README.rst')):
            with open(os.path.join(self.context, 'README.rst'), 'w', encoding="utf-8") as rst:
                rst.write(self.name)

        if not os.path.exists(os.path.join(self.context, 'README.md')):
            with open(os.path.join(self.context, 'README.md'), 'w', encoding="utf-8") as md:
                md.write("# %s" % self.name)
