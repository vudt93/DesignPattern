from abc import ABC, abstractmethod


class Remote(ABC):

    @abstractmethod
    def get_data(self):
        pass
