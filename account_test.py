import unittest 
from account import Account 


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Ahmed","Mukhtar","abc234","mukhtarabdirahman@gmail.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Ahmed")
        self.assertEqual(self.new_account.user_name,"Mukhtar")
        self.assertEqual(self.new_account.password,"abc234")
        self.assertEqual(self.new_account.email,"mukhtarabdirahman@gmail.com")