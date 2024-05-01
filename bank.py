class Bank():
    def __init__(self, name, branch) -> None:
        self.name = name
        self.branch = branch
        self.customers = []
        self.total_asset = 0
        self.total_loan = 0

    def add_account(self, account):
        account.account_number = len(self.customers)+100
        self.customers.append(account)

    def add_asset(self, ammount):
        self.total_asset += ammount

    def withdraw_asset(self, ammount):
        if self.total_asset >= ammount:
            self.total_asset-=ammount
            return True
        else: 
            print('The Bank is Bankrupt!')
            return False

    def find_account(self, email):
        account = list(filter(lambda x: x.email == email, self.customers))
        return account
    
    def delete_account(self, account_email):
        customer = self.find_account(account_email)
        if len(customer) > 0:
            self.customers.remove(customer[0])
            print('Delete Success!')
        else:
            print('Account Not Found')

    def show_customer(self):
        print(f"Name\t\tEmail\tAccount_Type\tAccount_number\tBalance")
        print('-------------------------------------------------------------')
        for customer in self.customers:
            print(f"{customer.name}\t{customer.email}\t{customer.account_type}\t{customer.account_number}\t{customer.balance}")

    def check_balance(self):
        print(f"Total Bank Balance: {self.total_asset}");
    
    def check_Loan(self):
        print(f"Total Bank Loan: {self.total_loan}");
    
    def is_loan_available(self, ammount):
        if (self.total_asset - self.total_loan) >= ammount:
            print("Loan Available")
        else:
            print("Loan is not Available")

    def __repr__(self) -> str:
        return f"Welcome from {self.name}, {self.branch} Branch"