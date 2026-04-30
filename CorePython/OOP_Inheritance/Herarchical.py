class Shape:
    def __init__(self,color,border_width):
        self.color = color
        self.border_width = border_width              # base class

    def get_Color(self):
        return self.color
    def get_borde(self):
        return self.border_width

class Rectangle(Shape):
    def __init__(self,length,width,color,border_width):  # child class 1
        self.length = length
        self.width = width
        super().__init__(color, border_width)

    def get_length(self):
        return self.length
    def get_width(self):
        return self.width

class Circle(Shape):
    def __init__(self,radius,color,border_width):     #   child class 2
        self.radius = radius
        super().__init__(color,border_width)

    def get_cir(self):
        return self.radius

rec = Rectangle(5,4,"Red",52)
cir = Circle(4,"Blue",41)

print(rec.get_Color())
print(rec.get_borde())
print(rec.get_length())
print(rec.get_width())

print(cir.get_Color())
print(cir.get_borde())
print(cir.get_cir())