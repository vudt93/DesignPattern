from Builder.Builder import Builder
from Builder.Motorbike import Motorbike


class MotorbikeBuilder(Builder):
    product = Motorbike()

    def build_name(self):
        self.product.name = "Motorbike"

    def build_type(self):
        self.product.type = "Gas"

    def get_product(self):
        return self.product
