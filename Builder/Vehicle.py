from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def print(self):
        pass
