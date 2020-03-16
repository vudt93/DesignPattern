class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_car(self):
        self.builder.build_name()
        self.builder.build_model()

    def build_motorbike(self):
        self.builder.build_name()
        self.builder.build_type()