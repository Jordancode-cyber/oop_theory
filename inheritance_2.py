class Phone:
    def __init__(self, brand, at):
        self.brand = brand
        self.at = at
    def load_at(self, amount):
        self.at = self.at + amount
a = Phone("iPhone", 1000)
b = Phone("Tecno", 2000)

a.load_at(3000)
print(f"Airtime balance: {a.at}UGX")


class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def show_details(self):
        return self.amount
        print(f"{self.name} your current balance is {self.amount}")

    def add_money(self, deposit):
        if deposit <= 0:
             return
        self.amount += deposit
        print(f"Deposit of {self.amount}UGX successfull.")

    def withdraw_money(self, withdraw):
        self.withdraw = self.amount - withdraw
        print(f"Withdraw of {self.amount}UGX successfull.")
    def get_balance(self):
         return self.amount
    
client1 = BankAccount("Joram", 10000)
deposit1 = client1.add_money(20000)
withdraw1 = client1.withdraw_money(12000)
print(f"Current balance: {client1.amount}UGX")


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
            print(f"My name is {self.name}, my email is {self.email}")

    def send_email(self, message):
            print(f" to:{self.email}, {message}")

# class Student(Person):
#     pass

class Lecturer(Person):
    def teach(self, course_name):
        print(f"{self.name} is teaching {course_name}")

L1 = Lecturer("Moses Ayebare", "moses@email.com")
L1.introduce()

# print(isinstance(S1, Student))