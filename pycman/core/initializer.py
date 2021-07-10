from __future__ import annotations

import abc
import os
import re
from typing import List


class InitError(BaseException):
    pass


class AbstractBuilder(metaclass=abc.ABCMeta):
    builders_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "builders")

    def __init__(self):
        pass

    @staticmethod
    def get_builders() -> List[AbstractBuilder]:
        from pycman.utils.common import import_module

        builders = []
        for module in os.listdir(AbstractBuilder.builders_path):
            if os.path.isdir(os.path.join(AbstractBuilder.builders_path, module)):
                continue
                
            builder = import_module(os.path.splitext(module)[0], AbstractBuilder.builders_path)
            builders.append(builder.Builder())

        builders.sort(key=lambda x: x.order())
        return builders

    @abc.abstractmethod
    def build(self, initializer: PycmanInitializer):
        pass

    @abc.abstractmethod
    def order(self) -> int:
        pass

    def __eq__(self, other):
        return self.order() == other.order()

    def __lt__(self, other):
        return self.order() < other.order()

    def __gt__(self, other):
        return self.order() > other.order()


class PycmanInitializer:

    def __init__(self, context: str, name: str = None, author: str = None, email: str = None):
        """
        初始化设置，这里用来初始化项目信息，
        最基本要素：项目名，作者，邮箱
        """

        if not context:
            raise InitError("self.context unknown")

        self.context = context

        if name is None:
            self.name = input('Project name: ')
            if not self.name:
                raise InitError("Project name can't be empty.")
        else:
            self.name = name

        if author is None:
            self.author = input('Author: ')
            if not self.author:
                raise InitError("Author can't be empty.")
        else:
            self.author = author

        if email is None:
            self.email = input('Email: ')
            if not self.email:
                raise InitError("Email can't be empty.")
        else:
            self.email = email

        rex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(rex, self.email):
            raise InitError("Email Invalid.")

        self.init()

    def __do_build(self):
        builders = AbstractBuilder.get_builders()
        for builder in builders:
            builder.build(self)

    def init(self):
        from pycman.utils import print_logo
        print_logo()
        print('==> PycmanInitializer started')
        self.__do_build()
        print('==> All done.')
