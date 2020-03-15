from abc import ABC, abstractmethod


class ProductA(ABC):

    @abstractmethod
    def print(self):
        pass
