from pycman.builder import get_builder
from pycman.builder.BaseBuilder import Director


def build(name='GeneralBuilder'):
    builder = get_builder(name)
    director = Director(builder())
    director.build()
