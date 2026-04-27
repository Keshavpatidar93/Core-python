class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        className = self.__class__.__name__
        print("destroying class name ",className)

    def __str__(self):
        return  "Person : name = %s, age = %s " % (self.name,self.age)

P11 = Person('keshav',18)
P22 = Person('anshu',14)

print(P11)
print(P22)