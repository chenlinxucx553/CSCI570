__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/29/2020 5:34 PM'

import abc


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


class PCFacotry(object):
    def produce(self):
        return PC()


class LapTopFacotry(object):
    def produce(self):
        return LapTop()


if __name__ == '__main__':
    pc = PCFacotry().produce()
    laptop = LapTopFacotry().produce()
    pc.info()
    laptop.info()

    for _ in range(10):
        print(PCFacotry().produce())
