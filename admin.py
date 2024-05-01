from user import User

class Admin(User):
    def __init__(self, name, email, address, type) -> None:
        super().__init__(name, email, address)
        self.type = type

    def create_account(self, bank, user):
        bank.add_account(user)
        print("Account Create Successful!")

    def find_account(self, bank, user_email):
        customer = bank.find_account(user_email)
        if len(customer) > 0: 
            print(customer[0])
        else:
            print('Not Found')

    def delete_account(self, bank, account_email):
        bank.delete_account(account_email)

    def check_balance(self, bank):
        bank.check_balance()
    
    def check_Loan(self, bank):
        bank.check_Loan()

    def is_loan_available(self, bank, ammount):
        bank.is_loan_available(ammount);
    
    def show_customer(self, bank):
        bank.show_customer()

    def __repr__(self) -> str:
        return f'Welcome Admin {self.name}'
