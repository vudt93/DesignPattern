from AbstractFactory.AnotherFactory import AnotherFactory
from AbstractFactory.AnotherFactoryParallelA import AnotherFactoryParallelA
from AbstractFactory.AnotherFactoryParallelB import AnotherFactoryParallelB
from AbstractFactory.ConcreteFactory import ConcreteFactory
from AbstractFactory.ConcreteFactoryParallelA import ConcreteFactoryParallelA
from AbstractFactory.ConcreteFactoryParallelB import ConcreteFactoryParallelB


def create_family_product(factory):
    productA = factory.produce('A')
    productA.print()
    productB = factory.produce('B')
    productB.print()
    
    
factory = ConcreteFactory()
create_family_product(factory)

another_factory = AnotherFactory()
create_family_product(another_factory)


def create_family_product_parallel_factory(factory_parallel_a, factory_parallel_b):
    productA = factory_parallel_a.produce()
    productB = factory_parallel_b.produce()
    productA.print()
    productB.print()


factory_parallel_a = ConcreteFactoryParallelA()
factory_parallel_b = ConcreteFactoryParallelB()
create_family_product_parallel_factory(factory_parallel_a, factory_parallel_b)

another_factory_parallel_a = AnotherFactoryParallelA()
another_factory_parallel_b = AnotherFactoryParallelB()
create_family_product_parallel_factory(another_factory_parallel_a, another_factory_parallel_b)

