import os
import sys
import textwrap

CONTEXT = os.path.abspath(os.getcwd())


def init_meta_data(builder):
    builder.entry = input('Entry ( main.py ): ')
    if not builder.entry:
        builder.entry = 'main.py'
        open(os.path.join(CONTEXT, builder.name, 'main.py'), 'w').close()


def init_requirements(builder):
    print(' -> create requirements.txt...')
    default_requirements = ['fire']
    with open(os.path.join(CONTEXT, builder.name, 'requirements.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(default_requirements))


def init_package_module(builder):
    print(' -> create package.py...')
    with open(os.path.join(CONTEXT, builder.name, 'package.py'), 'w', encoding='utf-8') as f:
        f.write(textwrap.dedent("""
        package = {
            'name': '%s',
            'version': '0.0.0',
            'author': '%s',
            'email': '%s',
            'scripts': {
                'dev': 'python %s',
                'default': 'echo 请输入明确的命令名称'
            }
        }
            """) % (builder.name, builder.author, builder.email, builder.entry))


def init_venv(builder):
    print(' -> create venv...')
    os.system('python -m venv %s' %
              os.path.join(CONTEXT, builder.name, 'venv'))


def init_git(builder):
    print(' -> create git repository...')
    os.chdir(os.path.join(CONTEXT, builder.name))
    os.system('git init')
    print(' -> create .gitignore...')
    default_ignores = ['venv/', '__pycache__/']
    with open(os.path.join(CONTEXT, builder.name, '.gitignore'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(default_ignores))


def init_pbr(builder):
    pbr_cfg = textwrap.dedent("""
    [metadata]
    name = %s
    author = %s
    author-email = %s
    summary = ...
    license = MIT
    description-file = 
        README.rst
    home-page = http://example.com
    requires-python = >= 3.4

    [files]
    packages = 
        package


    [entry_points]
    console_scripts =
        cmd=package.module:function
    """ % (builder.name, builder.author, builder.email))

    setup_script = textwrap.dedent("""
    import setuptools
    setuptools.setup(setup_requires=['pbr'], pbr=True)
    """)
    with open(os.path.join(CONTEXT, builder.name, 'setup.cfg'), 'w', encoding="utf-8") as cfg:
        cfg.write(pbr_cfg)

    with open(os.path.join(CONTEXT, builder.name, 'setup.py'), 'w', encoding="utf-8") as cfg:
        cfg.write(setup_script)


def init_readme(builder):
    pass
