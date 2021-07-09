import os

from pycman.core import PycmanInitializer
from pycman.core.initializer import AbstractBuilder


class Builder(AbstractBuilder):
    def order(self) -> int:
        return 4

    def build(self, initializer: PycmanInitializer):
        """
        初始化git
        请在 package_module 初始化完成后调用
        Args:
            initializer:

        Returns:

        """
        if 'package.py' not in os.listdir():
            os.chdir(initializer.context)

        # if '.git' not in os.listdir():
        #     os.system('git init')

        if '.gitignore' not in os.listdir():
            print(' -> create .gitignore...')
            default_ignores = ['venv/', '__pycache__/',
                               '*.ini', '.eggs/', '*.egg-info', 'dist/', 'build/']
            with open(os.path.join(initializer.context, '.gitignore'), 'w', encoding='utf-8') as f:
                f.write('\n'.join(default_ignores))
