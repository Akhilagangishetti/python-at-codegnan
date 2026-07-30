# Deposite Function
def Deposite(account:int, deposite_amount:int)->str:

    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} deposite successful and current balance is:{users[account]['balance']}"