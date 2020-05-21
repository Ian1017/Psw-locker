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
        Users.users_list.append(self)