import unittest
from user_credentials import User, Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that defines test cases for the class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User('Pop', 'Smoke', 'big092')# create user object


    def test__init__(self):
        '''
        Test to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.first_name, "Pop")
        self.assertEqual(self.new_user.last_name, "Smoke")
        self.assertEqual(self.new_user.password, "big092")


    def test_save_user(self):
        '''
        Test case to test if the user object is saved to the users list.
        '''
        self.new_user.save_user()
        


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credential = Credentials("Pop", "Instagram", "realpopsmoke", "woobackbaby")


    def test__init__(self):
        '''
        Test case to check if creation of credential instances is properly done.
        '''

        self.assertEqual(self.new_credential.user_name, "Pop")
        self.assertEqual(self.new_credential.site_name, "Instagram")
        self.assertEqual(self.new_credential.account_name, "realpopsmoke")
        self.assertEqual(self.new_credential.password, "woobackbaby")


    def test_save_credentials(self):
        '''
        Test case to check if we can save credentials to the credentials list.
        '''

        self.new_credential.test_save_credential()
        facebook = credentials("Lawsons", "Facebook", "william", "mombasa@69")
        facebook.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)


    
    def test_display_credentials(self):
        '''
        Test case to test if our objects show.
        '''

        self.new_credential.save_credential()
        facebook = Credentials("Lawsons", "Facebook", "william", "mombasa@69")
        facebook.save_credential()
        gmail = Credentials('Jane','Gmail','maryjoe','pswd200')
        gmail.save_credential()
        self.assertEqual(len(Credentials.display_credential(facebook.user_name)), 2)



if __name__ == '__main__':
    unittest.main()
