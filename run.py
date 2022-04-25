#!/usr/bin/env python3.10.4
from Credentiallocker import Credentials
from Userlocker import Users
def create_user(username, login_password):
    '''
    Function to create new user
    '''
    new_user = Users(username, login_password)
    return new_user

def add_user(user):
    '''
    Function to save user
    '''
    user.add_user()

def remove_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(username):
    ''' 
    Function to find user by username
    '''
    return Users.find_by_username(username)

def check_existing_user(username, login_password):
    ''' 
    Function to authenticate user
    '''
    return Users.user_exists(username, login_password)

def create_credentials(application_name, account_username, account_password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(application_name, account_username, account_password)
    return new_credentials

def add_credentials(new_credentials):
    '''
    Function to save credentials
    '''
    new_credentials.add_credentials()

def remove_credentials(new_credentials):
    '''
    Function to delete credentials
    '''
    new_credentials.delete_credentials()

def display_credentials():
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_credentials()

def check_existing_credentials(application_name):
    '''
    Function to check that credentials for a certain application exist
    '''
    return Credentials.credentials_exist(application_name)

def find_credentials(application_name):
    '''
    Function that finds credentials using the application name
    '''
    return Credentials.find_by_application_name(application_name)

def generate_a_password(passwordLength):
    '''
    Function that generates random password of 8 characters
    '''
    return Credentials.generate_password(passwordLength)
