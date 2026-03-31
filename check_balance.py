from bank.data import accounts
def check_balance(account_number):
    if account_number in accounts:
        balance=accounts[account_number]["balance"]
        print(f"the balance for account number {account_number} is {balance}")