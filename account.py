from datetime import date
from user import User

class Account(User):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.balance = 0
        self.account_type = account_type
        self.transections = []
        self.loan_history = []
        self.account_number = None

    def transection(self, data):
        self.transections.append(data)

    def transection_history(self):
        print('Type\tAmmount\tDate\t')
        print('-----------------------')
        for transection in self.transections:
            print(f"{transection['type']}\t{transection['ammount']}\t{transection['date']}")

    def withdraw(self, ammount, bank):
        if ammount > self.balance:
            print("Withdrwal Ammount Exceeded!")
        else:
            w = bank.withdraw_asset(ammount)
            if w:
                self.balance -= ammount
                self.transection({'type': 'withdraw', 'ammount': ammount, 'date':date.today()})
                print(f"Withdraw: {ammount}, Balance: {self.balance}")

    def receive(self, ammount, name):
        self.balance += ammount
        self.transection({'type': 'Recived', 'ammount': ammount, 'date':date.today()})
        print(f"{ ammount} Ammount Received from {name} is Successful")

    def add_money(self, ammount, bank):
        self.balance += ammount
        bank.add_asset(ammount)
        self.transection({'type': 'Add', 'ammount': ammount, 'date':date.today()})
        print(f"{ammount} Added Your Account")

    def take_loan(self, ammount):
        if len(self.loan_history) < 2:
            self.balance+=ammount
            self.transection({'type': 'Loan', 'ammount': ammount, 'date':date.today()})
            self.loan_history({'ammount': ammount, 'date': date.today(), 'deadline': date(2025, 12, 12)})
        else:
            print('You have Taken already 2 loan')

    def transfer(self, ammount, to_email, bank):
        if ammount <= self.balance:
            to = bank.find_account(to_email)
            if len(to) > 0:
                to[0].receive(ammount, self.name)
                self.balance -= ammount
                self.transection({'type': 'Send', 'ammount': ammount, 'date':date.today()})
                print(f"Sending Money From Your Account {ammount} is Successful")
            else:
                print('Account Not Found')
        else: 
            print("Your Balance is Insufficient")

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def __repr__(self) -> str:
        return f"Welcome: {self.name} Balance: {self.balance}"