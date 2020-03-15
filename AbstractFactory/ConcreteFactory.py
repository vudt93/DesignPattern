from Factory.ConcreteProductA import ConcreteProductA
from Factory.ConcreteProductB import ConcreteProductB
from Factory.Factory import Factory


class ConcreteFactory(Factory):
    def produce(self, type):
        if type == 'A':
            return ConcreteProductA()
        if type == 'B':
            return ConcreteProductB()
