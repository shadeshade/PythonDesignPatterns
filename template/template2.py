from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print("Abstract says: Operation 1")

    def base_operation2(self):
        print("Abstract says: Operation 2")

    def base_operation3(self):
        print("Abstract says: Operation 3")

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass


class ConcreteClassA(AbstractClass):
    def required_operation1(self):
        print("Concrete Class A says: Operation 1")

    def required_operation2(self):
        print("Concrete Class A says: Operation 2")


class ConcreteClassB(AbstractClass):
    def required_operation1(self):
        print("Concrete Class B says: Operation 1")

    def required_operation2(self):
        print("Concrete Class B says: Operation 2")

    def hook1(self):
        print("Concrete Class B: Overriden hook 1")


def client_code(abstract_class):
    abstract_class.template_method()


if __name__ == '__main__':
    concrete_a = ConcreteClassA()
    client_code(concrete_a)

    print("")

    concrete_b = ConcreteClassB()
    client_code(concrete_b)