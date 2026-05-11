import pickle

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, "\t", self.name, "\t", self.salary)


with open("../file/employee.txt", 'wb') as file:       # it can't be written as file = open("hj/njbh/j/","rb")  as the operation is same and it run in here but not into the Deserilization
    emp = Employee(1, 'Keshav', 500000)
    pickle.dump(emp, file)