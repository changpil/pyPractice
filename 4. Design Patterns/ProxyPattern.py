import abc
class Greeter(abc.ABC):

    @abc.abstractmethod
    def greet(self):
        pass

class RealGreeter(Greeter):
    def __init__(self, name):
        self.name = name
    def greet(self):
        return str("Hello " + self.name)

class GreaterProxy(Greeter):
    greeter = None
    def greet(cls, name):
        if cls.greeter == None:
            cls.greeter = RealGreeter(name)
        else:
            cls.greeter.name = name
        return cls.greeter.greet()


proxy = GreaterProxy()
print(proxy.greet("Chang"))
