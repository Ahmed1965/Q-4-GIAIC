# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, to be implemented by subclasses
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Implementing the abstract method
rectangle_area = Rectangle(5, 10)
print(f'The area of the rectangle is: {rectangle_area.area()}')
        