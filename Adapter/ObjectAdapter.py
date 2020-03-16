from Adapter.Target import Target


class ObjectAdapter(Target):
    _adaptee = None

    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def name(self):
        return self._adaptee.name

    @property
    def age(self):
        return self._adaptee.age

    @property
    def address(self):
        return "{} {}".format(self._adaptee.street_num, self._adaptee.street_name)