import os

from pycman.core import PycmanInitializer
from pycman.core.initializer import AbstractBuilder


class Builder(AbstractBuilder):
    def order(self) -> int:
        return 2

    def build(self, initializer: PycmanInitializer) -> None:
        """
        创建Readme文档
        """
        print(' -> create readme docs...')
        if not os.path.exists(os.path.join(initializer.context, 'README.rst')):
            with open(os.path.join(initializer.context, 'README.rst'), 'w', encoding="utf-8") as rst:
                rst.write(initializer.name)

        if not os.path.exists(os.path.join(initializer.context, 'README.md')):
            with open(os.path.join(initializer.context, 'README.md'), 'w', encoding="utf-8") as md:
                md.write("# %s" % initializer.name)
