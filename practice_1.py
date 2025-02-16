class Accounnt():
    #Constructor
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
     #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Amount debited", amount)
        print("total balance",self.get_balance())
    
    def credited(self,amount):
        self.balance += amount
        print("Amount credited", amount)
        print("total balance",self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1=Accounnt(12000, 123456)
acc1.debit(1000)
acc1.credited(5000)
print(acc1.get_balance())
# print(acc1.balance)
# print(acc1.acc_no)