import os
import shutil
import stat
import unittest

from pycman.cli import run
from pycman.initializer import PycmanInitializer


def rmtree(folder: str):
    def _readonly_handler(func, path, execinfo):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    if os.path.exists(folder):
        shutil.rmtree(folder, onerror=_readonly_handler)


class TestPycmanInitializer(unittest.TestCase):
    context = os.path.dirname(os.path.abspath(__file__))

    def setUp(self) -> None:
        os.chdir(self.context)
        self.demo_project = "TestProject"
        if not os.path.exists(self.demo_project):
            os.mkdir(self.demo_project)

        self.context = os.path.join(self.context, self.demo_project)
        os.chdir(self.context)

    def test_init(self):
        PycmanInitializer(self.context, "test", "singein", "singein@xxx.com")
        self.assertTrue(os.path.exists(os.path.join(self.context, "package.py")))
        self.assertTrue(os.path.exists(os.path.join(self.context, ".gitignore")))
        self.assertTrue(os.path.exists(os.path.join(self.context, "README.md")))
        self.assertTrue(os.path.exists(os.path.join(self.context, "README.rst")))
        self.assertTrue(os.path.exists(os.path.join(self.context, "setup.cfg")))
        self.assertTrue(os.path.exists(os.path.join(self.context, "setup.py")))

    def test_run_scripts(self):
        data = run()
        self.assertEqual(data, "请输入明确的命令名称\n")

    def tearDown(self) -> None:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        if os.path.exists(self.context):
            rmtree(self.context)
