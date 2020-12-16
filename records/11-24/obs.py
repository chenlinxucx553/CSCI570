from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class Subject(ABC):
    @abstractmethod
    def append(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def get_content(self):
        pass


class SubjectA(Subject):

    def __init__(self):
        self._observers = []
        self.content = None

    def append(self, observer: Observer):
        self._observers.append(observer)

    def remove(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        self.content = randrange(0, 10)
        print("Current Content is -- > {}".format(self.content))
        self.notify()

    def get_content(self):
        return self.content


class CustomerA(Observer):
    def update(self, subject: Subject):
        if subject.get_content() % 2 == 0 or subject.get_content() >= 5:
            print("ConcreteObserverA: Reacted to the event")


class CustomerB(Observer):
    def update(self, subject: Subject):
        if subject.get_content() % 2 != 0 or subject.get_content() < 5:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = SubjectA()

    a = CustomerA()
    subject.append(a)

    b = CustomerB()
    subject.append(b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.remove(a)

    subject.some_business_logic()
