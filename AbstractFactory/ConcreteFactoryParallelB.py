from Factory.ConcreteProductB import ConcreteProductB
from Factory.FactoryParallel import FactoryParallel


class ConcreteFactoryParallelB(FactoryParallel):
    def produce(self):
        return ConcreteProductB()
