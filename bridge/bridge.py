# Bridge design pattern

from __future__ import annotations

from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return ("Abstraction: default operation with: \n "
                "{}".format(self.implementation.operation_implementation()))


class ExtendedAbstraction(Abstraction):

    def operation(self):
        return ("ExtendedAbstraction: extended default operation with: \n "
                "{}".format(self.implementation.operation_implementation()))


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self):
        pass


class ConcreteImplementation1(Implementation):
    def operation_implementation(self):
        return "Concrete 1: Here is my result"


class ConcreteImplementation2(Implementation):
    def operation_implementation(self):
        return "Concrete 2: Here is my result"


def client_code(abstraction):
    print(abstraction.operation(), end="")


if __name__ == '__main__':

    implementation = ConcreteImplementation1()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementation2()
    abstraction = Abstraction(implementation)
    client_code(abstraction)