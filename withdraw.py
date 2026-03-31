from bank.data import accounts

def withdraw(account_number, amount):
    if account_number not in accounts:
        print("account not found")
        return

    if accounts[account_number]["balance"] >= amount:
        accounts[account_number]["balance"] -= amount
        print("withdrawn {} from account number {} successfully".format(amount, account_number))
    else:
        print("insufficient funds")
