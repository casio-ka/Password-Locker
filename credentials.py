class User:
    '''
    Class that generated new instances of Users
    '''
    # empty contact list
    user_list = [] 

    def __init__(self,user_name,password,full_name,email):

        '''
        Method to define the properties each user object holds
        '''
        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.email = email

    def save_user(self):
        '''
		Function to save a newly created user instance
		'''

        User.user_list.append(self)    


    def delete_user(self):
        '''
		Function to delete a saved user instance
		'''
        User.user_list.remove(self)   


    @classmethod
    def find_by_name(cls,name):
        '''
		Class method to find users from the list of users saved
		'''
        for user in cls.user_list:
            if user.user_name == name:
                return user  


    @classmethod
    def user_exist(cls,name):
        '''
		Class method to check if users exist from the list of users saved
		'''
       
        for user in cls.user_list:
            if user.password == name:
                    return user

        return False      


    @classmethod
    def display_user(cls, user_name):  
        '''
		Class method to display the list of users saved
		'''
       
        return cls.user_list