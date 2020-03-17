from Decorator.Decorator import Decorator


class ConcreteDecorator2(Decorator):
    def do_operation(self):
        print("Decorate 2 Start")
        self.component.do_operation()
        print("Decorate 2 End")
