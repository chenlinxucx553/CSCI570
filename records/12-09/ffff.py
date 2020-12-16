__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/9/2020 4:18 PM'

from abc import abstractmethod


class Product(object):

    @abstractmethod
    def setMsg(self, msg="default info"):
        self.msg = msg

    @abstractmethod
    def info(self):
        print(self.msg)


class DefaultObj(Product):

    def __init__(self):
        super().setMsg()


class Factory(object):
    @abstractmethod
    def produce(self):
        return DefaultObj()


class PC(Product):
    def __init__(self):
        self.setMsg('pc info')


class LAPTOP(Product):
    def __init__(self):
        self.setMsg('laptop info')


class PCFactory(Factory):
    def produce(self):
        return PC()


class LAPTOPFactory(Factory):
    def produce(self):
        return LAPTOP()


if __name__ == '__main__':
    ss = Factory().produce()
    pc = PCFactory().produce()
    laptop = LAPTOPFactory().produce()
    pc.info()
    laptop.info()

    ss.info()
