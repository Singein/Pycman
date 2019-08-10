from contextlib import contextmanager
import os

_context = os.path.abspath(os.getcwd())
@contextmanager
def context(cwd):
    os.chdir(cwd)
    print('==> cwd %s' % os.getcwd())
    yield
    os.chdir(_context)
    print('==> cwd %s' % os.getcwd())


with context(os.path.dirname(_context)):
    open('hello-contextlib.txt', 'w').close()
  