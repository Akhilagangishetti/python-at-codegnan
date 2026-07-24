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
    pass


# login function
def login(account:int, password:str)-> bool:
    pass

#get balance
def balance(acoount:int)-> str:
    pass

#get withdrawal
def withdrawal(account:int)-> str:
    pass

#get current