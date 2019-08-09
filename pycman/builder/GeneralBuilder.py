from builder.BaseBuilder import BaseBuilder, InitError
import os
import textwrap


CONTEXT = os.path.abspath(os.getcwd())


class Builder(BaseBuilder):

    def init_meta_data(self):
        self.name = input('Project name: ')
        if not len(self.name):
            raise InitError("project name can't be empty.")

        self.author = input('Author: ')
        if not len(self.author):
            raise InitError("author can't be empty.")

        self.email = input('Email: ')
        self.entry = input('Entry ( main.py ): ')
        if not self.entry:
            self.entry = 'main.py'
            open(os.path.join(CONTEXT, self.name, 'main.py'), 'w').close()

    def init_requirements(self):
        print(' -> create requirements.txt...')
        default_requirements = ['fire']
        with open(os.path.join(CONTEXT, self.name, 'requirements.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(default_requirements))

    def init_project_manager(self):
        print(' -> create package.py...')
        with open(os.path.join(CONTEXT, self.name, 'package.py'), 'w', encoding='utf-8') as f:
            f.write(textwrap.dedent("""
                package_info = {
                    'name': '%s',
                    'version': '0.0.0',
                    'author': '%s',
                    'email': '%s'
                }

                scripts = {
                    'dev': 'python %s',
                    'default': 'echo 请输入明确的命令名称'
                }
                """) % (self.name, self.author, self.email, self.entry))

    def init_venv(self):
        print(' -> create venv...')
        os.system('python -m venv %s' %
                  os.path.join(CONTEXT, self.name, 'venv'))

    def init_git(self):
        print(' -> create git repository...')
        os.system('git init')
        print(' -> create .gitignore...')
        default_ignores = ['venv/', '__pycache__/']
        with open(os.path.join(CONTEXT, self.name, '.gitignore'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(default_ignores))

    def init_pbr(self):
        pbr_cfg = textwrap.dedent("""[metadata]
        name = %s
        author = %s
        author-email = %s
        summary = ...
        license = MIT
        description-file = 
            README.rst
        home-page = http://example.com
        requires-python = >= 3.4
        classifier =
            Development Status:: 4 - Beta
            Environment:: Console
            Environment:: OpenStack
            Intended Audience:: Developers
            Intended Audience:: Information Technology
            License: : OSI Approved : : Apache Software License
            Operating System:: OS Independent
            Programming Language:: Python

        [files]
        packages = 
            package


        [entry_points]
        console_scripts =
            cmd=package.module:function
        """ % (self.name, self. author, self.email))

        setup_script = textwrap.dedent("""import setuptools
        setuptools.setup(setup_requires=['pbr'], pbr=True)
        """)
        with open(os.path.join(CONTEXT, self.name, 'setup.cfg'), 'w', encoding="utf-8") as cfg:
            cfg.write(pbr_cfg)

        with open(os.path.join(CONTEXT, self.name, 'setup.py'), 'w', encoding="utf-8") as cfg:
            cfg.write(setup_script)

    def init_readme(self):
        pass
