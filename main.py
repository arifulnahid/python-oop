from bank import Bank
from account import Account
from admin import Admin

isb = Bank(name='ISB', branch='BD')
manager = None

def customer():
    email = input('Enter Your Email: ')
    d = isb.find_account(email=email)
    if len(d) > 0:
        user = d[0]
        print(f'Welcome {user.name}!')

        while True:
            print('\n-------------------------------')
            print('1. Show Profile')
            print('2. Check Balanace')
            print('3. Add Money')
            print('4. Withdraw')
            print('5. Send Money')
            print('6. Transection History')
            print('7 Take Loan')
            print('8. Back')
            print('-------------------------------\n')

            option = input('Enter a Option: ')
            
            match option:
                case '1':
                    print(user)
                case '2':
                    user.check_balance()
                case '3':
                    ammount = int(input('Enter a Ammount: '))
                    user.add_money(ammount, isb)
                case '4':
                    ammount = int(input('Enter a Ammount: '))
                    user.withdraw(ammount, isb)
                case '5':
                    ammount = int(input('Enter a Ammount: '))
                    to_email = input('Enter a Email: ')
                    user.transfer(ammount, to_email, isb)
                case '6':
                    user.transection_history()
                case '7':
                    ammount = int(input('Enter a Ammount: '))
                    user.take_loan(ammount)
                case '8':
                    break
                case _:
                    break
    else:
        print('Account Not Found')




def admin(admin):
    if admin is None:
        name = input('Enter Your Name: ')
        email = input('Enter Your Email: ')
        address = input('Enter Your Address: ')
        account_type = input('Enter Account Type (Savings/Current): ')

        admin = Admin(name=name, email=email, address=address, type=account_type)
    
    print(f'Welcome admin {admin.name}!')
     
    while True:
        print('\n-------------------------------')
        print('1. Create: ')
        print('2. Find Account: ')
        print('3. Delete: ')
        print('4. Check Balance: ')
        print('5. Check Loan: ')
        print('6. Check Loan Available: ')
        print('7. Show All Account: ')
        print('8. Back')
        print('-------------------------------\n')

        option = input('Enter a Option: ')

        match option:
            case '1':
                name = input('Enter Customer Name: ')
                email = input('Enter Customer Email: ')
                address = input('Enter Customer Address: ')
                account_type = input('Enter Account Type (Savings/Current): ')

                customer = Account(name=name, email=email, address=address, account_type=account_type)
                admin.create_account(isb, customer)

            case '2':
                find_email = input('Enter a Email: ')
                admin.find_account(isb, find_email)
            case '3':
                account_email = input('Enter a Email: ')
                admin.delete_account(isb, account_email)
            case '4':
                admin.check_balance(isb)
            case '5':
                admin.check_Loan(isb)
            case '6':
                ammount = int(input('Enter a Ammount: '))
                admin.is_loan_available(isb, ammount)
            case '7':
                admin.show_customer(isb)
            case '8':
                break
            case _:
                break

    return admin

while True:
    print(f"Welcome To {isb.name}!")
    print('\n-------------------------------')
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    print('-------------------------------\n')

    option = input("Enter a option: ")

    match option:
        case '1':
            customer()
        case '2':
           manager =  admin(manager)
        case '3':
            break
        case _:
            break
