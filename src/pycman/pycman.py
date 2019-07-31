import os


# BASE_DIR = os.path.abspath(__file__)

CONTEXT = os.path.abspath(os.getcwd())


def init_guide():
    name = input('Project name: ')
    return name


def init(projectName=None):
    projectName = projectName or init_guide()
    # print(CONTEXT)
    os.mkdir(projectName)
    print('==> init project[%s]' % projectName)
    open(os.path.join(CONTEXT, projectName, 'requirements.txt'), 'w')
    open(os.path.join(CONTEXT, projectName, 'package.ini'), 'w')
    print(' -> init python venv...')
    os.system('python -m venv %s' % os.path.join(CONTEXT, projectName, 'venv'))
    print('Done.')


def run(script=None):
    import importlib
    import sys
    script = script or 'default'
    sys.path.append(CONTEXT)
    pro = importlib.__import__('pro')
    os.system(pro.scripts[script])


# init()
run()
