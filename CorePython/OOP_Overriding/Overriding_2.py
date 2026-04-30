class Shape:
    def execute(self):
        print("Calling execute method of Shape class ..")
        self.area()

    def area(self):
        print("Calling area method of Shape class ..")


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        rec_area = self.length * self.width
        print("The area of the rectangle is :",rec_area)



class Circle(Shape):
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        cir_area = 3.14 * self.radius **2
        print("The area of the circle is :",cir_area)


class Test(Shape):
    pass           # it return the control to the Shape class( area method ) as there is nothing into the Test class

r = Rectangle(12,5)
r.execute()   # it print the area of rectangle class as self means obj of the same class through which the object of same class is created

c = Circle(5)
c.execute()

t = Test()
t.execute()