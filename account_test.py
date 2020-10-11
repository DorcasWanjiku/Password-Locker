import unittest 
from account import Account 


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Dorcas","Wanjiku","sh3k1l33","smallwanjiku@gmail.com") 

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Dorcas")
        self.assertEqual(self.new_account.user_name,"Wanjiku")
        self.assertEqual(self.new_account.password,"sh3k1l33")
        self.assertEqual(self.new_account.email,"smallwanjiku@gmail.com")
        def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []    


    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","46578907890","test@user.com") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)