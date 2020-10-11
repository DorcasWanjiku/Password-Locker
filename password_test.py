import unittest 
from user import Users
from credential import Credentials 

class TestUsers(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Users("DorcasWanjiku", "sh3k1l33")
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"DorcasWanjiku")
        self.assertEqual(self.new_user.password,"sh3k1l33")
        
            
        
class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the credential behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_credential = Credentials("small_wanjiku", "Instagram", "DorcasWanjiku", "github") 
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"small_wanjiku")
        self.assertEqual(self.new_credential.account,"Instagram")
        self.assertEqual(self.new_credential.account_username,"DorcasWanjiku")
        self.assertEqual(self.new_credential.account_password,"github")

if __name__== '__main__':
    unittest.main()        
        
    
    
