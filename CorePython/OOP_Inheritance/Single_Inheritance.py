class Shape:
    def __init__(self):
        self.color = " "
        self.borderwith = 0

    def set_color(self,color):
        self.color = color
    def set_borderwidth(self,borderwidth):
        self.borderwidth = borderwidth

    def get_color(self):
        return self.color
    def get_borderwidth(self):
        return self.borderwidth

class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def set_length(self,length):
        self.length = length
    def set_width(self,width):
        self.width = width

    def get_length(self):
        return self.length
    def get_width(self):
        return self.width

r = Rectangle()
r.set_length(10)
r.set_width(7)
r.set_color("Black")
r.set_borderwidth(5)

print("The length of the rectangle is :",r.get_length())
print("The width of the rectangle is :",r.get_width())
print("The area of the rectangle is :",r.get_length() * r.get_width())
print("The color is :",r.get_color())
print("The borderwidth is :",r.get_borderwidth())
