class Account:
    def __init__(self):
        self.number = 0
        self.type = " "
        self.balance = 0
        # self.amount = 0

    def set_number(self,number):
        print("Creating Account.....")
        self.number = number
    def get_number(self):
        return self.number

    def set_type(self,type):
        self.type = type
    def get_type(self):
        return self.type

    def set_balance(self,balance):
        self.balance = balance
    def get_balance(self):
        return self.balance

    def credit(self,amount):
        self.balance += amount
        print("your balance is :",self.balance)

    def debit(self,amount):
        self.balance -= amount
        print("your balance is :",self.balance)


acc = Account()
acc.set_number(88159)
acc.set_type("Saving")
acc.set_balance(50000)
print("Account number is :",acc.get_number())
print("Account type is :",acc.get_type())
print("Available balance in your account is :",acc.get_balance())
acc.debit(10000)
acc.credit(7777)