# Parent class
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Another child class inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of the child classes
rectangle = Rectangle("blue", 5, 4)
circle = Circle("red", 3)

# Calling methods of the child classes
print("Rectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
print("Circle:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
