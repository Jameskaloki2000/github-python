class Users:
    user_list=[]
    def __init__(self,username,login_password) :
        'Creates new password and username when initiallized'
        self.username=username
        self.password=login_password
    def save_password (self):
        Users.user_login.append(self)
        "A  deifintion that takes in the self object and pushed it to the created array to store the passord"
    
