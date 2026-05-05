from abc import ABC,abstractmethod
class Name(ABC):
    @abstractmethod
    def show(self):
        pass

class what(Name):
    def __init__(self,name):
        self.name = name


# if we does not override the abstract method of Abstract class in the child class the error occures
    # def show(self):
    #     print("The name is :",self.name)

c = what("Keshav")
c.show()