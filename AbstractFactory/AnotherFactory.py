from AbstractFactory.AnotherProductA import AnotherProductA
from AbstractFactory.AnotherProductB import AnotherProductB
from Factory.Factory import Factory


class AnotherFactory(Factory):
    def produce(self, type):
        if type == 'A':
            return AnotherProductA()
        if type == 'B':
            return AnotherProductB()
