from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Child Class: Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square area =", self.side * self.side)

    def perimeter(self):
        print("Square perimeter =", 4 * self.side)


# Child Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle area =", math.pi * self.radius * self.radius)

    def perimeter(self):
        print("Circle perimeter =", 2 * math.pi * self.radius)


# Creating Objects
s = Square(5)
c = Circle(3)

# Calling Methods
s.area()
s.perimeter()

c.area()
c.perimeter()