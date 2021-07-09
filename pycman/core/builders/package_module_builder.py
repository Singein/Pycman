import os

from pycman.core import PycmanInitializer
from pycman.core.initializer import AbstractBuilder

PACKAGE_CONTENTS = """
package = {
    'name': '%s',
    'version': '0.0.1',
    'author': '%s',
    'email': '%s',
    'scripts': {
        'default': 'echo hello!'
    }
}
""".strip()


class Builder(AbstractBuilder):
    def order(self) -> int:
        return 0

    def build(self, initializer: PycmanInitializer) -> None:
        """
        创建package.py
        """
        print(' -> create package.py...')
        with open(os.path.join(initializer.context, 'package.py'), 'w', encoding='utf-8') as f:
            f.write(PACKAGE_CONTENTS.strip() % (initializer.name, initializer.author, initializer.email))
