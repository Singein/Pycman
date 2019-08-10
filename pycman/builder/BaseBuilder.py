import abc


class InitError(BaseException):
    pass


class BaseBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init_meta_data(self):
        """init project metadata"""

    @abc.abstractmethod
    def init_requirements(self):
        """init project requirements.txt"""

    @abc.abstractmethod
    def init_project_manager(self):
        """create a templated package.py"""

    @abc.abstractmethod
    def init_venv(self):
        """create venv"""

    @abc.abstractmethod
    def init_git(self):
        """init git repository"""

    @abc.abstractmethod
    def init_pbr(self):
        """init setup.py and setup.cfg"""

    @abc.abstractmethod
    def init_readme(self):
        """init readme"""


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
