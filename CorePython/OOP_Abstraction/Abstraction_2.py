from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        a1 = 3.14 * self.radius ** 2
        print("The area of the Circle is :",a1)
        return a1

cir = Circle(5)
cir.area()

obj : Shape = Circle(4)
print("Printing the Area of circle using the refrence of Shape Class :",obj.area())