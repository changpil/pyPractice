import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

class Triangle(Shape):
    def draw(self):
        print("Triangle")

class Circle(Shape):
    def __init__(self, color):
        self.color =  color
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setRadius(self, r):
        self.radius = r

    def draw(self):
        print(f"Circle color {self.color} {self.x}:{self.y}")

class ShapeFactory:
    def __init__(self):
        self.circleMap = dict()

    def getCircle(self, color):
        if color not in self.circleMap:
            self.circleMap[color] = Circle(color)
            print("Creating circle of color : " + color)
        return self.circleMap[color]

import random
def main():
    colors = ["Red", "Green", "Blue", "White", "Black"]
    circleFactory = ShapeFactory()
    for i in range(20):
        circle = circleFactory.getCircle(random.choice(colors))
        circle.setX(random.randrange(0, 100))
        circle.setY(random.randrange(0, 100))
        circle.setRadius(random.randrange(0, 1000))
        circle.draw()

if __name__ == "__main__":
    main()