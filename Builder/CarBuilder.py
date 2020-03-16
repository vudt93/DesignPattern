from Builder.Builder import Builder
from Builder.Car import Car


class CarBuilder(Builder):
    product = Car()

    def build_name(self):
        self.product.name = "Car"

    def build_model(self):
        self.product.model = "4 Wheels"

    def get_product(self):
        return self.product
