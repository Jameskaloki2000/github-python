class Users:
    user_list=[]
    def __init__(self,username,login_password) :
        'Creates new password and username when initiallized'
        self.username=username
        self.password=login_password
    def add_user(self):
        '''
        add user details method saves user object into users list
        '''
        Users.users_list.append(self)
    def delete_user(self):
        '''
        delete user details method removes user object from users list
        '''
        Users.users_list.remove(self)
    @classmethod
    def find_by_username(cls, username):
        '''
        authenticate user username
        Args: 
        username : name used by user to login
        Returns: 
        user
        '''
        for user in Users.users_list:
            if user.username == username:
                return user