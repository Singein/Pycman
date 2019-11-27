import abc
import os


class InitError(BaseException):
    pass


class BaseBuilder(metaclass=abc.ABCMeta):

    # @abc.abstractmethod
    def init(self):
        """
        初始化设置，这里用来初始化项目信息，
        最基本要素：项目名，作者，邮箱
        """
        # TODO 加入校验
        self.name = input('Project name: ')
        if not len(self.name):
            raise InitError("project name can't be empty.")
        # os.mkdir(self.name)
        self.author = input('Author: ')
        if not len(self.author):
            raise InitError("author can't be empty.")
        self.email = input('Email: ')


    def before_build(self):
        pass

    @abc.abstractmethod
    def building(self):
        pass


    def finish(self):
        pass


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.init()
        self.builder.before_build()
        self.builder.building()
        self.builder.finish()
