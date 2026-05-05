class Person1:
    def Name(self):
        print("My name is Keshav ")

    def Surname(self):
        print("My surname is Patidar ")

    def Age(self):
        print("I am 19 year Old")


class Person2:
    def Name(self):
        print("My name is Rammmm ")

    def Surname(self):
        print("My surname is Chopda ")

    def Age(self):
        print("I am 39 year Old")

p1 = Person1()
p2 = Person2()

for i in [p1,p2]:   # at the run time the program changes it behaviour(dynamic) from one object to another
    i.Name()
    i.Surname()
    i.Age()