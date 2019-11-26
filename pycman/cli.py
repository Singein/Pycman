from pycman.build import build
import os
import fire

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


def release(sync: bool = False):
    """实现版本号标定，并提交代码

    Keyword Arguments:
        sync {bool} -- 如果sync为True, 则同步代码到远程仓库 (default: {False})
    """
    pass
    # 第一步实现版本标定


def commit():
    """
    使用commitizen进行代码提交
    """
    os.system('git add . && cz commit')


def main():
    fire.Fire({
        'create': create,
        'run': run
    })


if __name__ == "__main__":
    main()
