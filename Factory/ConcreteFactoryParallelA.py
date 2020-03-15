from Factory.ConcreteProductA import ConcreteProductA
from Factory.FactoryParallel import FactoryParallel


class ConcreteFactoryParallelA(FactoryParallel):
    def produce(self):
        return ConcreteProductA()
