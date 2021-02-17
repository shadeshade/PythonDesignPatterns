class Source:

    def request(self):
        return "Source: Default source behavior"


class Adaptee:

    def specific_request(self):
        return "Adaptee: Adaptee behavior"


class Adapter(Source, Adaptee):

    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(source):
    print(source.request(), end="")

if __name__ == '__main__':

    print("Client: I can work with source objects")

    source = Source()
    client_code(source)
    print("\n")

    adaptee = Adaptee()
    print("Client: I don't understand the interface of the Adaptee")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: I can work with the Adaptee using the Adapter")

    adapter = Adapter()
    client_code(adapter)