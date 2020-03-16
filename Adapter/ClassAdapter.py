from Adapter.Adaptee import Adaptee
from Adapter.Target import Target


class ClassAdapter(Adaptee, Target):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return "{} {}".format(self._street_num, self._street_name)
