from Decorator.Component import Component


class ConcreteComponent(Component):
    def do_operation(self):
        print("Operation")