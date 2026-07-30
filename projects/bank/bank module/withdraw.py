# withdraw function
def withdraw(account:int, withdraw_amount:int)-> str:
    curr_balance = users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdraw successful and current balance is:{users[account]['balance']}"
    return "Insufficent Balance"