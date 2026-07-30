# Data base
"""
users = {
            Account:{
                     'name':Username,
                     'email': user email,
                     'balance': 5000,
                     'password']: password
                }
            }
"""

users = {
    1001:{'name':"Akhila",'email': 'akhilagangishetti2@gmail.com' ,'balance':5000,'password': 1001},
    1002:{'name':"Vanitha",'email': 'vanithagangishetti2@gmail.com' ,'balance':5000,'password': 1001},          
     }


# Register Functions
def register(username:str, email:str, balance:int, password:str)->str:
    return "Register page under development process"


# login function
def login(account:int, password:str)-> bool:
    if account in Users:
        if user[account]['password'] == password:
            return True
        return False
    return False

#get balance
def balance(acoount:int)-> str:
    curr_balance = user[account]['balance']
    return f"Curret Balance is:{curr_balance}"

# withdraw function
def withdraw(account:int, withdraw_amount:int)-> str:
    curr_balance = users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdraw successful and current balance is:{users[account]['balance']}"
    return "Insufficent Balance"

# Deposite Function
def Deposite(account:int, deposite_amount:int)->str:

    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} deposite successful and current balance is:{users[account]['balance']}"
    
    

# Transfer Function
def transfer(from_acc:int, transfer_amount:int)->str:
    print("user in transfer page")


# Ministatement Function
def Ministatement(account:int):
    print("user in ministatement page")

# Logout Function
def logout():
    print("Bye Bye buddy, see you later")
    exit()


# main
if __name__ == "__main__":
    print("Welcome to the Mini Bank")
    print("1. Login \n 2. Register")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        # call Login function
        account = int(input("Enter Your Account Number:"))
        password = input("Enter Your Password:")
        login_val = login(account=account, password=password)
        while login_val:

            print("1.Get Balance \n 2. Withdraw \n 3. Deposite \n 4. Transfer \n 5. Ministatement \n 6. Logout")
            choice = int(input("Enter your Choice:"))
            if choice == 1:
                #call Balance Functions
                print(balance(account=account))
            elif choice == 2:
                amount = int(input("Enter Withdraw amount:"))
                print(withdraw(account=account, withdraw_amount=amount))
            
             
            elif choice == 3:
                amount = int(input("Enter Deposite amount:"))
                print(Deposite(account=account, deposite_amount=amount))
            
            elif choice == 4:
                Reciver = int(input("Enter Reciever Account Number:"))
                amount = int(input("Enter Transfer amount:"))
                print(transfer(from_acc=account,
                                to_acc=reciever,
                                transfer_amount=account))
            elif choice == 5:

                print(Ministatement(account=account))

            elif choice == 6:
                print(logout())
            else:
                print("Select your choice in between 1-6")
        else:
            print("Invalid Login Credentials")
    elif choice == 2:
        username = input("Enter User name:")
        email = input("Enter User email id:")
        initial_deposite = int(input("Enter the initial Deposite amount:"))
        password = input("Enter your new password:")
        print(register(username=username,
                       email=email,
                       balance=initial_deposite,
                       password=password))
    else:
        print("Invalid choice, please select 1 or 2")
      