__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/29/2020 5:47 PM'

import abc


class Factory(abc.ABC):
    @abc.abstractmethod
    def produce(self):
        return DefaultObj()


class Product(abc.ABC):
    @abc.abstractmethod
    def info(self):
        pass


class PC(Product):
    def info(self):
        print("This is a PC")


class DefaultObj(Product):
    def info(self):
        print("This is a DefaultObj")


class LapTop(Product):
    def info(self):
        print("This is a LapTop")


class PCFacotry(Factory):
    def produce(self):
        return PC()


class LapTopFacotry(Factory):
    """
    if you dont claim this method, you will get a
        TypeError: Can't instantiate abstract class LapTopFacotry with abstract methods produce

    if you want to use father class logic, you need to use super(), like this:
        def produce(self):
            return super(LapTopFacotry, self).produce()

    """

    def produce(self):
        return super(LapTopFacotry, self).produce()

    def customized_produce(self):
        return LapTop()


if __name__ == '__main__':
    pc = PCFacotry().produce()
    laptop = LapTopFacotry().customized_produce()
    pc.info()
    laptop.info()

    for _ in range(10):
        print(PCFacotry().produce())
