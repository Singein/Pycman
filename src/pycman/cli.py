from initial import init_project
import os
import fire

CONTEXT = os.path.abspath(os.getcwd())


def create():
    init_project()


def run(script=None):
    import importlib
    import sys
    script = script or 'default'
    sys.path.append(CONTEXT)
    pro = importlib.__import__('package')
    os.system(pro.scripts[script])


if __name__ == "__main__":
    fire.Fire({
        'create': create,
        'run': run
    })
