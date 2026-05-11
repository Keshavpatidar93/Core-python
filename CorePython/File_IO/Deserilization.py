import pickle
from Serilization import Employee

with open("../file/employee.txt", 'rb') as file:
    obj = pickle.load(file)
    print("Printing Employee information after deserilization")

obj.display()