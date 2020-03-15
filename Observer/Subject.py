from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def subcribe(self):
        pass

    @abstractmethod
    def unsubcribe(self):
        pass

    @abstractmethod
    def notify_all(self):
        pass
