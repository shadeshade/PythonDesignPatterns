from __future__ import annotations

from abc import ABC, abstractmethod
from random import randrange


class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _state = None
    _observers = []

    def attach(self, observer):
        print("Subject: Attached and observer")
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def logic(self):
        print("Doing something that matters")
        self._state = randrange(0, 10)

        print("State changed to {}".format(self._state))
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class ConcretedObserver1(Observer):
    def update(self, subject):
        if subject._state < 5:
            print("Observer 1 reacted to the event")


class ConcretedObserver2(Observer):
    def update(self, subject):
        if subject._state >= 5:
            print("Observer 2 reacted to the event")


if __name__ == '__main__':
    subject = ConcreteSubject()

    observer1 = ConcretedObserver1()
    subject.attach(observer1)

    observer2 = ConcretedObserver2()
    subject.attach(observer2)

    subject.logic()
    subject.logic()

    subject.detach(observer1)

    subject.logic()
