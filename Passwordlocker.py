class PasswordLocker:
    Credentials=[]
    def __init__(self,username,password) :
        'Creates new password and username when initiallized'
        self.username=username
        self.password=password
    def save_password (self):
        PasswordLocker.Credentials.append(self)
        "A  deifintion that takes in the self object and pushed it to the created array to store the passord"
