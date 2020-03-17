from Decorator.Decorator import Decorator


class ConcreteDecorator(Decorator):
    def do_operation(self):
        print("Decorate 1 Start")
        self.component.do_operation()
        print("Decorate 1 End")
