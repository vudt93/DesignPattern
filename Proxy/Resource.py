from abc import ABC, abstractmethod


class Resource(ABC):

    @abstractmethod
    def get_file_content(self):
        pass
