from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def print(self):
        pass
