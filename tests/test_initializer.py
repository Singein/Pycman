import os
import shutil

from pycman.cli import run
from pycman.core import PycmanInitializer
from pycman.utils import goto

cwd = os.path.dirname(os.path.abspath(__file__))
demo_project = "pycman_demo"


def test_initializer():
    with goto(cwd):
        if os.path.exists(demo_project):
            shutil.rmtree(demo_project, ignore_errors=True)

        os.mkdir(demo_project)
        initializer_cwd = os.path.join(cwd, demo_project)

        initializer: PycmanInitializer = PycmanInitializer(initializer_cwd, name="pycman_demo",
                                                           author="pycman",
                                                           email="singein@pycman.com")
        initializer.init()
        with goto(initializer_cwd):
            assert os.path.exists(os.path.join(initializer_cwd, "package.py"))
            assert os.path.exists(os.path.join(initializer_cwd, "tests"))
            assert os.path.exists(os.path.join(initializer_cwd, "requirements.txt"))
            assert os.path.exists(os.path.join(initializer_cwd, "README.md"))
            assert os.path.exists(os.path.join(initializer_cwd, "setup.cfg"))
            assert os.path.exists(os.path.join(initializer_cwd, "setup.py"))

            assert run() == "Please specify a command alias. 请指定一条指令别名。"

        shutil.rmtree(initializer_cwd, ignore_errors=True)
