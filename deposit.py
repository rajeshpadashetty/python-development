from bank.data import accounts
def deposit(account_number,amount):
    if account_number in accounts:
        accounts[account_number]["balance"]+=amount
        print(f'deposited {amount} to account number {account_number} successfully')