import unittest # Importing the unittest module
from Credentiallocker import Credentials
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for Credentials class behaviours
    
    Args:
        unittest.TestCase: TestCase class that  helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_credentials = Credentials("Twitter", "James", "Malla")
    def test_initialization(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.application_name, "Twitter")
        self.assertEqual(self.new_credentials.account_username, "James")
        self.assertEqual(self.new_credentials.account_password, "Malla")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []

    def test_add_multiple_credentials(self):
        '''
        test_add_multiple_credentials to check if we can save multiple credential objects to our credentials list
        '''
        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "John", "10")
        test_credentials.add_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)
    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from credentials list
        '''
        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "Alfred", "101")
        test_credentials.add_credentials()

        test_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
    def test_display_all_credentials(self):
        '''
        test method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
    def test_find_by_application_name(self):
        '''
        test to check if we can find a credentials by application name
        '''
        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "Alfred", "101")
        test_credentials.add_credentials()

        found_credential = Credentials.find_by_application_name("Instagram")
        self.assertEqual(found_credential.account_username, test_credentials.account_username)
