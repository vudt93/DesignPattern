from Builder.Vehicle import Vehicle


class Car(Vehicle):
    name = ""
    model = ""

    def print(self):
        print(self.name + " " + self.model)
