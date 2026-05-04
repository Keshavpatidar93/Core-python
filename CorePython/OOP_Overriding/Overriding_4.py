class Shape:
    def area(self):
        print("Area method of the Shape class........")

class Circle(Shape):
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        Cir_area = Circle.pi*self.radius**2
        print("The area of the circle is :",Cir_area)

class Triangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        Tri_area = self.length*self.width
        print("The area of the Triangle is :",Tri_area)

class Test(Shape):
    pass
#
# obj1 = [Circle(5),Triangle(5,2),Test()]
# for i in obj1:
#     i.area()

# obj2 : list[Shape] = [Circle(5),Triangle(5,2),Test()]
# for i in obj2:
#     i.area()
#
obj3 : list[Test] = [Circle(5),Triangle(5,2),Test()]        # in these the list of test class is created and the object comes like circle but the Test
for i in obj3:                                                           # class does not have the Circle but as we see,the test class inherits property of Shape class and the area
    i.area()                                                            # of circle is called so the Shape class checks is there is any circle class if yes it called its area method

