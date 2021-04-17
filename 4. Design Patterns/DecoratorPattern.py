import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

class Triangle(Shape):
    def draw(self):
        print("Triangle")

class Circle(Shape):
    def draw(self):
        print("Circle")

# Decorator was not needed to be inherited from Shape in Python.
# In Java, inheritance forces to implement parent methods to child Decorators.
class Decorator(Shape):
    def __init__(self, shape):
        self.shape = shape

class ColorDecorator(Decorator):
    def __init__(self, shape, color):
        super().__init__(shape)
        self.color = color

    def draw(self):
        print(self.color)
        self.shape.draw()
        print(self.color)

class PatternDecorator(Decorator):
    def __init__(self, shape, pattern):
        super().__init__(shape)
        self.pattern = pattern

    def draw(self):
        print(self.pattern)
        self.shape.draw()
        print(self.pattern)

s = Circle()
s.draw()
print("*"*100)
cd = ColorDecorator(s, "red")
cd.draw()
print("*"*100)
pd = ColorDecorator(Triangle(), "Polca dot")
pd.draw()
print("*"*100)