import os

from pycman.core.initializer import AbstractBuilder, PycmanInitializer


class Builder(AbstractBuilder):
    def order(self) -> int:
        return 6

    def build(self, initializer: PycmanInitializer) -> None:
        """
        创建测试文件夹
        """
        tests_dir = os.path.join(initializer.context, 'tests')
        if os.path.exists(tests_dir) and os.path.isdir(tests_dir):
            return
        os.mkdir(os.path.join(initializer.context, 'tests'))
