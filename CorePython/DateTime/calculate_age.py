import datetime
today = datetime.date.today()
dof = datetime.date(2007,5,20)
age = today.year - dof.year
born_day = dof.strftime("%A")
print("Your age is : ",age)
print("Your born day is : ",born_day)
