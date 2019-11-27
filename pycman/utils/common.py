"""
本模块包含了一些基本的常用且通用的工具函数
author: singein
e-mail: singein@outlook.com
"""

import importlib
import os
from contextlib import contextmanager


class ContextError(BaseException):
    pass


@contextmanager
def goto(path: str):
    """用于切换工作区

    Arguments:
        path {str} -- 目标工作区路径

    Raises:
        ContextError: 工作区切换时找不到路径时触发
    """
    cwd = os.getcwd()
    if not os.path.exists(path):
        raise ContextError(
            'Workspace switching error: the path does not exist')
    os.chdir(path)
    yield
    os.chdir(cwd)


def import_module(module: str = 'package', cwd: str = None) -> object:
    """动态导入指定工作目录 cwd 下的模块 

    Keyword Arguments:
        module {str} -- 模块名称 (default: {'package'})
        cwd {str} -- 解释器当前工作目录 (default: {None})

    Returns:
        object -- 返回该模块
    """
    os.sys.path.append(cwd)
    with goto(cwd):
        module = importlib.import_module(module)

    return module
