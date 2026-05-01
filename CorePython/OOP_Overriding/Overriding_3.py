class Shape:
    def execute(self):
        if self.validation():
            self.area()
        else:
            print("Invalid Condition....")

    def validation(self):
        print("Validation Method of the Shape Class.....")
        return False

    def area(self):
        print("Area Method of the Shape Class....")



class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def validation(self):
        if self.length > 0 and self.width > 0:
            return True
        else:
            return False

    def area(self):
        rec_area = self.length * self.width
        print("The area of the rectangle is :",rec_area)


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    pi = 3.14

    def validation(self):
        if self.radius > 0:
            return True
        else:
            return False

    def area(self):
        cir_area =  Circle.pi * self.radius ** 2
        print("The area of the circle is :",cir_area)


class Test(Shape):
    pass


rec = Rectangle(12,6)
rec.execute()

cir = Circle(12)
cir.execute()

tes = Test()
tes.execute()

invalid_rec = Rectangle(12,-6)
invalid_rec.execute()

invalid_cir = Circle(-5)
invalid_cir.execute()
