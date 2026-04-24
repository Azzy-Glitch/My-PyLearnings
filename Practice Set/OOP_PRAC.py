class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self._account_holder = account_holder
        self._balance = 0
        self._transactions = [] 

        self.balance = initial_balance 

    # Getter
    @property
    def balance(self):
        return self._balance

    # Setter with validation
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    # Read-only property 
    @property
    def account_type(self):
        return "Savings Account"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self._transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transactions.append(f"Withdrawn: {amount}")

    def transaction_history(self):
        return self._transactions


Name = input("Enter Account Name: ") 
Balance = int(input("Enter initial Amount: "))

acc = BankAccount(Name, Balance)

acc.deposit(500)

acc.withdraw(200)

print(acc.balance)