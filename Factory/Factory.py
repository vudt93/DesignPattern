from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def produce(self, type):
        pass