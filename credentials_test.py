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