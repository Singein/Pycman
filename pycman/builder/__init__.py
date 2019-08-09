import importlib
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class BuilderNotFound(BaseException):
    pass


def get_builder(name):
    try:
        builder = importlib.__import__(name)
        return builder.Builder
    except ImportError:
        raise BuilderNotFound('Builder [%s] not found!' % name)
