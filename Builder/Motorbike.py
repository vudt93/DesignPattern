from Builder.Vehicle import Vehicle


class Motorbike(Vehicle):
    name = ""
    type = ""

    def print(self):
        print(self.name + " " + self.type)
