from abc import ABC, abstractmethod


class FactoryParallel(ABC):

    @abstractmethod
    def produce(self):
        pass
