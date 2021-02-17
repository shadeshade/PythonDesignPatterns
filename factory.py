from abc import ABC, abstractmethod


class IChair(ABC):
    @abstractmethod
    def get_demensions(self):
        """get chair sizes"""


class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.length = 80

    def get_demensions(self):
        return f"{self.__class__.__name__} demensions: height {self.height}, " \
               f"width {self.width}, length {self.length}"


class SmallChair(IChair):

    def __init__(self):
        self.height = 40
        self.width = 40
        self.length = 40

    def get_demensions(self):
        return f"{self.__class__.__name__} demensions: height {self.height}, " \
               f"width {self.width}, length {self.length}"


class ChairFactory:

    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype == "BigChair":
                return BigChair()
            elif chairtype == "SmallChair":
                return SmallChair()
            raise AssertionError(f"{chairtype} not found")
        except AssertionError as e:
            print(e)


b_chair = ChairFactory().get_chair("BigChair")
print(b_chair.get_demensions())
s_chair = ChairFactory().get_chair("SmallChair")
print(s_chair.get_demensions())
#dies after exception!
