import importlib
import os
import sys

from pycman.builder.BaseBuilder import BaseBuilder, Director, InitError
from pycman.builder import utils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class BuilderNotFound(BaseException):
    pass


def get_builder(name: str) -> object:
    """返回指定名称的的Builder, 当前Builder类型
    可以在builder模块下按照Builder模板扩充

    Arguments:
        name {str} -- builder模块所在的文件名

    Raises:
        BuilderNotFound: builder模块找不到时触发

    Returns:
        object -- 返回一个动态加载的builder类
    """
    try:
        builder = importlib.__import__(name)
        return builder.Builder
    except ImportError:
        raise BuilderNotFound('Builder [%s] not found!' % name)


def build(name='GeneralBuilder'):
    builder = get_builder(name)
    director = Director(builder())
    director.build()


__all__ = [
    'build',
    'BaseBuilder',
    'Director',
    'InitError',
    'utils'
]
