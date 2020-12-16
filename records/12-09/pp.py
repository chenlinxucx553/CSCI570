__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/9/2020 4:01 PM'

import random
from abc import abstractmethod


class Subject(object):
    def __init__(self):
        self.observes = []
        self.val = None

    def append(self, a):
        self.observes.append(a)

    def remove(self, a):
        self.observes.remove(a)

    def getVal(self):
        return self.val

    def have_something_to_tell(self):
        self.val = random.randrange(1, 10)
        print("we are going to publish {} st product".format(self.val))

        for obs in self.observes:
            obs.got_update(self)


class Customer(object):
    @abstractmethod
    def got_update(self, subject: Subject):
        pass


class CustomerA(Customer):
    def got_update(self, subject):
        if subject.getVal() % 2 == 0:
            print("customer A like it")


class CustomerB(Customer):
    def got_update(self, subject):
        if subject.getVal() % 2 != 0 or subject.getVal() < 5:
            print("customer B like it")


if __name__ == '__main__':
    subject = Subject()

    a = CustomerA()
    subject.append(a)

    b = CustomerB()
    subject.append(b)

    subject.have_something_to_tell()
    subject.have_something_to_tell()

    subject.remove(a)

    subject.have_something_to_tell()
