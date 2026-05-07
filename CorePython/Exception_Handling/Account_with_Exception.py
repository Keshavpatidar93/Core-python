class Withdrawl_time_exception(Exception):
    def __init(self,message):
        super().__init__(message)

class Deposit_time_exception(Exception):
    def __init__(self,message):
        super().__init__(message)

class Acount:
    def __init__(self):
        self.balance = 0
        self.count1 = 0
        self.count2 = 0

    def set_balance(self,balance):
        self.balance = balance
    def get_balance(self):
        return self.balance

    def deposite(self,amount):
        if amount > 300000:
            raise Deposit_time_exception("You can't deposite more than 3,00,000 in a single time  \n")

        if self.count1 >= 2:
            raise Deposit_time_exception("You can't deposite more than 2 times in a day  \n")

        else:
            print(f"The {amount} is adding into your balance ")
            self.balance += amount
            print(f"After adding the available balance is {self.balance}  \n")

    def withdraw(self,amount):
        if self.count2 >= 2:
            raise Withdrawl_time_exception("You cannot withdraw money more then 2 times in a day  \n")

        if amount > self.balance:
            raise Withdrawl_time_exception("You cannot have sufficient balance  \n")

        if amount > 200000:
            raise Withdrawl_time_exception("You Cannot withdraw more then 2,00,000 into a single transection  \n")

        if self.balance - amount < 2000:
            raise Withdrawl_time_exception("The minimum amount in account must be 2000  \n")

        else:
            print(f"The {amount} is succesfully withdraw from your account")
            self.balance -= amount
            self.count2 += 1
            print(f"After withdraw the amount available in your account is {self.balance}  \n")


acc = Acount()
acc.set_balance(5000)
print("The amount available in your account is :",acc.get_balance(),"\n")

try:
    acc.deposite(5000)
    acc.withdraw(7000)
    acc.withdraw(2500)      # here the exception occur as we don't have minimum 2000 in our account
    # acc.deposite(501234)
    # acc.withdraw(210000)   # here exception occur as we cant withdraw more than 200000

    #acc.deposite(500000)   # here the exception will occur as we can't deposite more than 3,00,000 in a single time

except Deposit_time_exception as ke:
    print("==>",ke)

except Withdrawl_time_exception as e:
    print("<==",e)

