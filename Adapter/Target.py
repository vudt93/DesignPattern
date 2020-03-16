class Target:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def address(self):
        return self._address
