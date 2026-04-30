class Acc:
    def __init__(self,number,balance):
        self.number = number
        self.balance = balance

class Trans(Acc):
    def __init__(self,cre,deb):
        super().__init__(123456,853)
        self.credit = cre
        self.debit = deb

ok = Trans(1000,500)
print(ok.credit)
print(ok.debit)
print(ok.number)
print(ok.balance)