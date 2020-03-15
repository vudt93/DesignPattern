from Factory.ConcreteFactory import ConcreteFactory
from Factory.ConcreteFactoryParallelA import ConcreteFactoryParallelA
from Factory.ConcreteFactoryParallelB import ConcreteFactoryParallelB

factory = ConcreteFactory()
productA = factory.produce('A')
productA.print()
productB = factory.produce('B')
productB.print()


factory_parallel_a = ConcreteFactoryParallelA()
factory_parallel_b = ConcreteFactoryParallelB()

productA = factory_parallel_a.produce()
productB = factory_parallel_b.produce()

productA.print()
productB.print()
