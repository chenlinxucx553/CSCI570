__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/29/2020 5:47 PM'

import abc


class Factory(abc.ABC):
    @abc.abstractmethod
    def produce(self):
        pass


class Product(abc.ABC):
    @abc.abstractmethod
    def info(self):
        pass


class PC(Product):
    def info(self):
        print("This is a PC")


class LapTop(Product):
    def info(self):
        print("This is a LapTop")


class PCFacotry(Factory):
    def produce(self):
        return PC()


class LapTopFacotry(Factory):
    def produce(self):
        return super(LapTopFacotry, self).produce()

    def customized_produce(self):
        return LapTop()


if __name__ == '__main__':
    pc = PCFacotry().produce()
    # laptop = LapTopFacotry().produce()
    laptop = LapTopFacotry().customized_produce()
    pc.info()
    laptop.info()

