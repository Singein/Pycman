from pycman.build import build
import os
import fire

CONTEXT = os.path.abspath(os.getcwd())


def create(project_type='GeneralBuilder'):
    build(project_type)


def run(script=None):
    import importlib
    import sys
    script = script or 'default'
    sys.path.append(CONTEXT)
    pro = importlib.__import__('package')
    os.system(pro.scripts.get(script, 'default'))


def build():
    """
    执行PBR构建
    """
    os.system('python setup.py bdist_wheel')


def release():
    pass


def commit():
    pass


def main():
    fire.Fire({
        'create': create,
        'run': run
    })


if __name__ == "__main__":
    main()
