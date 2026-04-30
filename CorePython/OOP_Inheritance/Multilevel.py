class Student:
    def Stu(self):
        self.name = input("Name is :")         # super class
        self.age = input("Age is :")
        self.college = input("College is :")

class Test(Student):
    def Tes(self):
        self.Adderess = input("Adderss is :")
        print("Enter the marks of the following subjects :")     # base class
        self.Hindi = int(input("Hindi :"))
        self.English = int(input("English :"))
        self.Maths = int(input("Maths :"))
        self.Physics = int(input("Physics :"))

class Marks(Test):
    def display(self):
        print("Your name is :",self.name)
        print("Your Age is :",self.age)
        print("Your College is :",self.college)               # child class
        print("Your Address is :",self.Adderess)
        print("Your Marks of Hindi is :",self.Hindi)
        print("Your Marks of English is :",self.English)
        print("Your Marks of Maths is :",self.Maths)
        print("Your Marks of Physics is :",self.Physics)

        total = (self.Hindi + self.English + self.Maths + self.Physics)
        if(total > 100):
            print("Passed ....")
        else:
            print("You are failed....")

        print("your total number is : ",total)

a  = Marks()
a.Stu()
a.Tes()
a.display()