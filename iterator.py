from abc import ABC, abstractmethod


class IIterator(ABC):
    @staticmethod
    @abstractmethod
    def next(self):
        """returns a next value etc."""

    @staticmethod
    @abstractmethod
    def has_next(self):
        """returns bool if the next value in collection"""


class Itarable(IIterator):
    def __init__(self, index, max_value):
        self.index = index
        self.max_value = max_value

    def next(self):
        if self.index < self.max_value:
            x = self.index
            self.index += 1
            return x
        else:
            raise Exception("AtEndOfTheIteratorException", "At end of iterator")

    def has_next(self):
        return self.index < self.max_value


ITARABLE = Itarable(0, 5)
print(ITARABLE.next())
print(ITARABLE.next())
print(ITARABLE.next())
print(ITARABLE.next())
print(ITARABLE.next())
# print(ITARABLE.next())

alist = [1,2,34,5]
it = iter(alist)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__())