from abc import ABC,abstractmethod        # library that can be imported to use the abstract class and method


class Shape(ABC):
    def execute(self):
        print("Execute Method of the Shape Class....")

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
       rect_area = self.length * self.width   # the area method must be override into the child class if we inherit the property from the class(abstract class)
       return rect_area

rec = Rectangle(4,6)
print("The area of the rectangle is :", rec.area())
