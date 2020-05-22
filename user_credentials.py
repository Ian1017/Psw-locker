import pyperclip
import random
import string

class User:
    '''
    Class that generates instances of user credentials
    '''

    users_list = [] #Empty list where users will be saved
    
    def __init__(self,first_name, last_name, password):
        '''
        __init__method that helps us define properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    def save_user(self):
        '''
        save_user method that saves user object in the users_list
        '''
        User.users_list.append(self)


class Credentials:
    '''
    Class that generates instances of account credentials, generate passwords and save information
    '''

    credentials_list = []
    users_credentials_list = []

    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method that checks if the name and password entered match entries in the users list.
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
        __init__ method that helps us define properties for our objects
        '''

        self.user_name = user_name
        self.site_name = site_name 
        self.account_name = account_name
        self.password = password


    def save_credentials(self):
        '''
        save_credential method that saves credential objects in the credentials_list
        '''

        Credentials.credentials_list.append(self)


    def generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lower + string.digits):
        '''
        Function to generate a 8 character password
        '''
        gen_password = ''.join(random.choice(char)for _in range(size))
        return gen_password
        

    @classmethod
    def display_credential(cls, user_name):
        '''
        Class method to show the list of credentials saved
        '''
        users_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                users_credentials_list.append(credential)
        return users_credentials_list


    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Class method that takes a site name and returns the credential that matches the site
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential



    @classmethod
    def copy_credential(cls, site_name):
        '''
        Class method that a copies a credential details after the credentials site_name has been entered
        '''
        find_credential = Credentials.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)