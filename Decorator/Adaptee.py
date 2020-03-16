class Adaptee:
    def __init__(self, name, age, street_num, street_name):
        self._name = name
        self._age = age
        self._street_num = street_num
        self._street_name = street_name

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def street_num(self):
        return self._street_num

    @property
    def street_name(self):
        return self._street_name

