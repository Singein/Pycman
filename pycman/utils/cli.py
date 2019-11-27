from pycman.builder import build
import os
import fire
from pycman.utils import mark_version

CONTEXT = os.path.abspath(os.getcwd())


def create(project_type: str = 'GeneralBuilder'):
    """按照流程模板，创建项目

    Keyword Arguments:
        project_type {str} -- 项目模板名称 (default: {'GeneralBuilder'})
    """
    build(project_type)


def init():
    """
    生成基本的pbr相关配置文件
    """
    pass


def run(script: str = None):
    """执行自定义脚本

    Keyword Arguments:
        script {[str]} -- 执行指定名称为 script 的指令 (default: {None})
    """
    import importlib
    import sys
    script = script or 'default'
    sys.path.append(CONTEXT)
    pro = importlib.__import__('package')
    os.system(pro.package["scripts"].get(script, 'default'))


def build():
    """
    执行PBR构建
    """
    os.system('python setup.py bdist_wheel')


def release():
    """
    实现版本号标定，并提交代码
    """
    version = mark_version()
    # 如果版本号标记成功， 执行构建
    if version:
        os.system('python setup.py bdist_wheel')
        os.system('git add .')
        os.system('git commit -m "docs(ChangeLog): update [%s]' % version)


def commit():
    """
    使用commitizen进行代码提交
    """
    os.system('git add . && cz commit')


def version():
    from pycman.utils import show_version
    show_version()


def entry_point():
    fire.Fire({
        'create': create,
        'init': init,
        'build': build,
        'run': run,
        'release': release,
        'commit': commit,
        'version': version
    })
