import random
import string 

class Credentials:
    '''
    class that generates new credentials
    '''
    credentials_list=[]
    def __init__(self,application_name,account_username,account_password):
        '''
         __init method that helps us define properties for our objects
        Args:
        application_name: New application name
        account_username: New account username
        account_password: New account password
        '''
        self.application_name = application_name
        self.account_username = account_username
        self.account_password = account_password
    def add_credentials(self):
        '''
        add_credentials method that saves credentials into credentials_list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        delete_credentials method that removes credentials from credentials_list
        '''
        Credentials.credentials_list.remove(self)
