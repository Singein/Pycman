import os
import sys
import textwrap

CONTEXT = os.path.abspath(os.getcwd())


def judge_path(context, builder, filename=''):
    """如果context最后一项和builder.name相同，
    忽略大小写, 便不指定新目录
    """
    
    # if builder.name.lower() == os.path.split(context)[-1].lower():
    if builder.in_place:
        return os.path.join(context,  filename)
    
    return os.path.join(context, builder.name, filename)


def init_meta_data(builder):
    builder.entry = input('Entry ( main.py ): ')
    if not builder.entry:
        builder.entry = 'main.py'
        open(judge_path(CONTEXT, builder, 'main.py'), 'w').close()


def init_requirements(builder):
    print(' -> create requirements.txt...')
    default_requirements = ['pycman']
    with open(judge_path(CONTEXT, builder, 'requirements.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(default_requirements))


def init_package_module(builder):
    print(' -> create package.py...')
    with open(judge_path(CONTEXT, builder, 'package.py'), 'w', encoding='utf-8') as f:
        f.write(textwrap.dedent("""
        package = {
            'name': '%s',
            'version': '0.0.1',
            'author': '%s',
            'email': '%s',
            'scripts': {
                'default': 'echo 请输入明确的命令名称'
            }
        }
            """) % (builder.name, builder.author, builder.email))


def init_venv(builder):
    print(' -> create venv...')
    os.system('python -m venv %s' % judge_path(CONTEXT, builder, 'venv'))


def init_git(builder):
    """
    请在 package_module 初始化完成后调用
    """
    print(' -> create git repository...')
    if 'package.py' not in os.listdir():
        os.chdir(judge_path(CONTEXT, builder))
    if not '.git' in os.listdir():
        os.system('git init')
    print(' -> create .gitignore...')
    default_ignores = ['venv/', '__pycache__/',
                       '*.ini', '.eggs/', '*.egg-info', 'dist/', 'build/']
    with open(judge_path(CONTEXT, builder, '.gitignore'), 'w', encoding='utf-8') as f:
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
    with open(judge_path(CONTEXT, builder, 'setup.cfg'), 'w', encoding="utf-8") as cfg:
        cfg.write(pbr_cfg)

    with open(judge_path(CONTEXT, builder, 'setup.py'), 'w', encoding="utf-8") as cfg:
        cfg.write(setup_script)


def init_readme(builder):
    with open(judge_path(CONTEXT, builder, 'README.rst'), 'w', encoding="utf-8") as rst:
        rst.write(builder.name)

    with open(judge_path(CONTEXT, builder, 'README.md'), 'w', encoding="utf-8") as md:
        md.write("# %s" % builder.name)
