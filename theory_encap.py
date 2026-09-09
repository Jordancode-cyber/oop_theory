class momowallet:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self._balance = balance

#Getter property for encapsulation
    @property
    def balance(self):
        return self._balance

#Setter property for encapsulation
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value



samuel_wallet = momowallet("Samuel", 5000)
print(f"{samuel_wallet.owner_name}'s wallet balance is: {samuel_wallet.balance}ugx")

