import abc


class InitError(BaseException):
    pass


class BaseBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init_meta_data(self):
        pass

    @abc.abstractmethod
    def init_requirements(self):
        pass

    @abc.abstractmethod
    def init_project_manager(self):
        pass

    @abc.abstractmethod
    def init_venv(self):
        pass

    @abc.abstractmethod
    def init_git(self):
        pass

    @abc.abstractmethod
    def init_pbr(self):
        pass

    @abc.abstractmethod
    def init_readme(self):
        pass


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.init_meta_data()
        self.builder.init_requirements()
        self.builder.init_project_manager()
        self.builder.init_venv()
        self.builder.init_git()
        self.builder.init_pbr()
        self.builder.init_readme()
