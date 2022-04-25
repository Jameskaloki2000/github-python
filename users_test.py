import unittest
from Userlocker import Users
class TestUsers(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = Users("James", "2000")
    def test_initialization(self):
        '''
        test_initialization case to test whether the object is being initialised properly
        '''
        self.assertEqual(self.new_user.username, "Lorna")
        self.assertEqual(self.new_user.login_password, "97")
    def test_add_user(self):
        '''
        test_add_user test case to test if the contact object is saved into the users list
        '''
        self.new_user.add_user()
        self.assertEqual(len(Users.users_list), 1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Users.users_list = []
    def test_add_multiple_users(self):
        '''
        test_add_multiple_users to check if we can save multiple user objects to our users_list
        '''
        self.new_user.add_user()
        test_user = Users("Samuel", "2000")
        test_user.add_user()
        self.assertEqual(len(Users.users_list), 2)    
if __name__ == '__main__':
    unittest.main()