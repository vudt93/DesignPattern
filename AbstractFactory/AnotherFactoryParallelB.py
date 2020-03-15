from AbstractFactory.AnotherProductB import AnotherProductB
from Factory.ConcreteProductB import ConcreteProductB
from Factory.FactoryParallel import FactoryParallel


class AnotherFactoryParallelB(FactoryParallel):
    def produce(self):
        return AnotherProductB()
