from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):

    def request(self):
        print("I'm the RealSubject, and I am processing the request")


class Proxy(Subject):

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Access granted")
        return True

    def log_access(self):
        print("Logging the time of request", end="")


def client_code(subject):
    subject.request()

if __name__ == '__main__':
    print("Client: I'm executing the client code with a real subject")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")
    print("Client: I'm executing the client code with a proxy")
    proxy = Proxy(real_subject)
    client_code(proxy)