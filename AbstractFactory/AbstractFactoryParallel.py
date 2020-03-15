from abc import ABC, abstractmethod


class AbstractFactoryParallel(ABC):

    @abstractmethod
    def produce(self):
        pass
