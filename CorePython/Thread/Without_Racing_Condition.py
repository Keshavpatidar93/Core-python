from time import sleep
from threading import *

class Account:
    def __init__(self):
        self.balance = 0

    def set_bal(self,bal):
        sleep(1)     # here it is neccesary as without it the first function dont wait so the first one is executed fully then the second function come
        self.balance = bal

    def get_bal(self):
        # sleep(1)
        return self.balance

    def deposite(self,amount):
        bale = self.get_bal()
        self.set_bal(bale + amount)


class Racing(Thread):
    def __init__(self,acc: Account, name):   #it taks the refrence of Account class and parameter is account
        super().__init__()
        self.account = acc
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposite(100)
            print(self.name,self.account.get_bal())

def main_fun():
    obj = Account()
    t1 = Racing(obj,"Keshav")
    t2 = Racing(obj,"Anshu")

    t1.start()
    t2.start()

    t1.join()  # it join all the two process at the end
    t2.join()

    print("The final Balance is :", obj.get_bal())


main_fun()