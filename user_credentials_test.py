import unittest
from user_credentials import User

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
        self.assertEqual(len(User.user_list, 1))


        

if __name__ == '__main__':
    unittest.main()
