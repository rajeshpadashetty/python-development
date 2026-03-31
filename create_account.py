from bank.data import accounts  
  
def create_account(account_number, account_holder, balance):  
    if account_number in accounts:  
        print("account already exists")  
    else:  
        accounts[account_number] = {  
            "account holder": account_holder,  
            "balance": balance  
        }  
        print("account created successfully") 
