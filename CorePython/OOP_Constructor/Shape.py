class Shape:
    def __init__(self):
        self.color = ''
        self.what = ''
        self.area = 0
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color

    def set_what(self,what):
        self.what = what
    def get_what(self):
        return self.what

    def set_area(self,area):
        self.area = area
    def get_area(self):
        return self.area

s1 = Shape()
s1.set_color("Red")
s1.set_what("Circle")
s1.set_area(987654.3210)
print(s1.get_color())
print(s1.get_what())
print(s1.get_area())