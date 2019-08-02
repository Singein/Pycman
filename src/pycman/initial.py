import os
import textwrap

CONTEXT = os.path.abspath(os.getcwd())


class InitError(BaseException):
    pass


def init_meta_data():
    name = input('Project name: ')
    if not len(name):
        raise InitError("project name can't be empty.")

    author = input('Author: ')
    if not len(author):
        raise InitError("author can't be empty.")

    email = input('Email: ')
    entry = input('Entry: ')

    return name, author, email


def init_requirements(name):
    print(' -> create requirements.txt...')
    default_requirements = [
        'fire', 'django'
    ]
    with open(os.path.join(CONTEXT, name, 'requirements.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(default_requirements))


def init_package(name, author, email):
    print(' -> create package.py...')
    with open(os.path.join(CONTEXT, name, 'package.py'), 'w', encoding='utf-8') as f:
        f.write(textwrap.dedent("""
            package_info = {
                'name': '%s',
                'version': '0.0.0',
                'author': '%s',
                'email': '%s'
            }

            scripts = {
                'zen': 'python -m this',
                'default': 'echo 请输入明确的命令名称'
            }
            """) % (name, author, email))


def init_venv(name):
    print(' -> create venv...')
    os.system('python -m venv %s' % os.path.join(CONTEXT, name, 'venv'))


def init_git(name):
    print(' -> create git repository...')
    os.system('git init')
    print(' -> create .gitignore...')
    default_ignores = ['venv/', '__pycache__/']
    with open(os.path.join(CONTEXT, name, '.gitignore'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(default_ignores))


def init_project():
    name, author, email = init_meta_data()
    print('==> init project[%s]' % name)
    print(' -> mkdir [%s]...' % name)
    os.mkdir(name)
    init_package(name, author, email)
    init_git(name)
    init_requirements(name)
    init_venv(name)
    print('Done.')
