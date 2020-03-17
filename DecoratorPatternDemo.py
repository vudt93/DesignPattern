from Decorator.ConcreteComponent import ConcreteComponent
from Decorator.ConcreteDecorator import ConcreteDecorator
from Decorator.ConcreteDecorator2 import ConcreteDecorator2

component = ConcreteComponent()
decorator = ConcreteDecorator(component)
decorator2 = ConcreteDecorator2(decorator)

decorator2.do_operation()