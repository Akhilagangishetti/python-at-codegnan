# login function
def login(account:int, password:str)-> bool:
    if account in Users:
        if user[account]['password'] == password:
            return True
        return False
    return False