class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def __add__(self, other):
        return BankAccount(self.balance + other.balance)
    
    def __sub__(self, amount):
        return BankAccount(self.balance - amount)
    
    def __str__(self):
        return f"Balance: {self.balance}"

acc1 = BankAccount(500)
acc2 = BankAccount(300)

acc3 = acc1 + acc2 
print(acc3)

acc4 = acc1 - 100
print(acc4)