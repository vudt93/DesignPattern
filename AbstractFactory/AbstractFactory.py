from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def produce(self, type):
        pass