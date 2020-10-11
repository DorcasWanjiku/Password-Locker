class Account:
    """
    Class that generates new instances of users.
    """
    account_list = [] 

    def __init__(self,account_name,user_name,password,email):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email
    

    def save_account(self):