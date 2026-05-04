class Shape:
    def area(self):
        print("The area method of the Shape class.....")

class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def set_len(self,length):
        self.length = length
    def set_width(self,width):
        self.width = width

    def get_len(self):
        return self.length
    def get_width(self):
        return self.width

    def area(self):
        print("The area of the Rectangle is :",self.length * self.width)

class Circle(Shape):
    def __init__(self):
        self.radius = 0

    def set_radius(self,radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def area(self):
        print("The area of the circle is :",3.14 * self.radius**2)


kes : list[Shape] = [Rectangle(),Circle()]

# obj1 = Rectangle()
# obj1.set_len(14)
# obj1.set_width(5)
# obj1.area()

obj1 : Rectangle = kes[0]
obj1.set_len(14)
obj1.set_width(5)

obj2 : Circle = kes[1]
obj2.set_radius(5)


for i in kes:
    i.area()