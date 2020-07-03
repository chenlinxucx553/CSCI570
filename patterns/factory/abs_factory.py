__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/29/2020 5:47 PM'

import abc


class Factory(abc.ABC):
    @abc.abstractmethod
    def produce_partA(self):
        return DefaultObj()

    def produce_partB(self):
        return DefaultObj()


class Product(abc.ABC):
    @abc.abstractmethod
    def info(self):
        pass


class PC_A(Product):
    def info(self):
        print("This is a PC_A")


class PC_B(Product):
    def info(self):
        print("This is a PC_B")


class DefaultObj(Product):
    def info(self):
        print("This is a DefaultObj")


class LapTop_A(Product):
    def info(self):
        print("This is a LapTop_A")


class LapTop_B(Product):
    def info(self):
        print("This is a LapTop_B")


class PCFacotry(Factory):
    def produce_partA(self):
        return PC_A()

    def produce_partB(self):
        return PC_B()


class LapTopFacotry(Factory):
    """
    if you dont claim this method, you will get a
        TypeError: Can't instantiate abstract class LapTopFacotry with abstract methods produce

    if you want to use father class logic, you need to use super(), like this:
        def produce(self):
            return super(LapTopFacotry, self).produce()

    """

    def produce_partA(self):
        return LapTop_A()

    def customized_produce(self):
        return super(LapTopFacotry, self).produce_partA()

    def produce_partB(self):
        return LapTop_B()


if __name__ == '__main__':

    for factory in [PCFacotry(), LapTopFacotry()]:
        part_a = factory.produce_partA()
        part_b = factory.produce_partB()
        ## do some manipulations
        part_a.info()
        part_b.info()
