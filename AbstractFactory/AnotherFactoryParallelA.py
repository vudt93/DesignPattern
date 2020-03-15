from AbstractFactory.AnotherProductA import AnotherProductA
from Factory.FactoryParallel import FactoryParallel


class AnotherFactoryParallelA(FactoryParallel):
    def produce(self):
        return AnotherProductA()
