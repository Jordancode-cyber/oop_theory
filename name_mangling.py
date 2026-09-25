class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

#Depositing money
    def deposit_money(self, amount):
        if amount <= 0:
            print(f"{self.owner} Deposit cannot be negative")
        return 
        self.__balance += amount
        print(f"{self.owner} Deposited: UGX {amount}")

#Withdraw money
    def withdraw_money(self, amount):
        if amount <= 0:
            print(f"{self.owner} Withdraw amount:")
        return
        if amount > self.__balance:
            print(f"Insufficeint funds")
        return
        self.__balance -= amount
        print(f"{self.owner} Withdraw: UGX {amount}")

account = BankAccount("Jordan", 50000)

#show the operation: depositing money
account.deposit_money(10000)
# account.deposit_money(-5000)

account.withdraw_money(10000)
# account.withdraw_money(-15000)

print(f"\nBalance: {account.get_balance()}")

