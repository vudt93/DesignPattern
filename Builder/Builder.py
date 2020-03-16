from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def build_name(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

    def build_type(self):
        pass

    def build_model(self):
        pass
