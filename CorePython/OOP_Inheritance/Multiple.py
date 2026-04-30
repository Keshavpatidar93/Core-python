class Addition:
    def sum(self,a,b):
        return  a+b                  # base class 1

class Subtraction:
    def sub(self,a,b):
        return a-b                  # base class 2

class Division(Addition,Subtraction):
    def div(self,a,b):
        if(b != 0):             # child class
            return a/b

obj = Division()
print(obj.sum(5,7))
print(obj.sub(9,1))
print(obj.div(72,8))