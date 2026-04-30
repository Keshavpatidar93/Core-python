class Shape:
    def area(self):
        print("The Shape class....")
        return print("Calling area method of Shape class ")

class Rectangle(Shape):
    pass
    # def area(self):
    #      print("The Rectangle class....")
    #      return print("Calling area method of Rectangle class")

# s = Shape()
# s.area()
#
# r = Rectangle()
# r.area()

obj: Shape = Rectangle()  # rectangle class ka object banaya (obj) Shape class ka refrence le ke
obj.area()   # kyuki Rectangle class me kuch nahi hai to usne parent class ko refer kar diya or uski method call kar di