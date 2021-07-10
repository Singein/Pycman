import fire
import os

CONTEXT = os.path.abspath(os.getcwd())


def init(context: str = '.'):
    """
    Initialize the scaffolding directly under the current folder, including:
     Create module, package.py, .gitignore, requirements.txt, pbr configuration.
    在当前文件夹下直接初始化脚手架， 包括:
    创建模块, package.py , .gitignore, requirements.txt, pbr配置。
    """
    from pycman.core import PycmanInitializer
    PycmanInitializer(context)


def run(script: str = None) -> str:
    """
    Execute custom script: pyc run <script>
    执行自定义脚本:  pyc run <script>

    Keyword Arguments:
        script {[str]} -- 执行指定名称为 script 的指令 (default: {None})
    """
    import importlib
    import sys

    sys.path.append(CONTEXT)
    pro = importlib.__import__('package')
    if not script:
        warning = "Please specify a command alias. 请指定一条指令别名。"
        print(warning)
        return warning

    return os.popen(pro.package["scripts"].get(script, 'default')).read()


def build():
    """
    Perform PBR construction, packaged as wheel format.
    执行PBR构建, 打包为wheel格式。
    """
    from pycman.utils import PYTHON
    os.system('%s setup.py bdist_wheel' % PYTHON)


def release():
    """
    Realize the version number calibration and submit the code.
    实现版本号标定，并提交代码。
    """
    from pycman.utils import mark_version
    from pycman.utils import PYTHON

    version: str = mark_version()
    # 如果版本号标记成功， 执行构建
    if version:
        os.system('%s setup.py bdist_wheel' % PYTHON)
        os.system('git add .')
        os.system('git commit -m "docs(ChangeLog): update ChangeLog about version[%s]"' % version)


def commit():
    """
    Use commitizen for code submission.
    使用commitizen进行代码提交。
    """
    from pycman.utils import PYTHON
    os.system('git add . && %s -m commitizen commit' % PYTHON)


def version():
    """
    View version number.
    查看版本号。
    """
    from pycman.utils import show_version
    show_version()


def entry_point():
    fire.Fire({
        # 'create': create,
        'init': init,
        'build': build,
        'run': run,
        'release': release,
        'commit': commit,
        'version': version
    })
