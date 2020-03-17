from Decorator.Component import Component


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def do_operation(self):
        if self.component is not None:
            self.component.do_operation()
