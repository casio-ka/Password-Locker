import pyperclip

# User Class
class User: # Class for all User Information
    """
    Class that generates new instances of users.
    """

    # Empty user list
    user_list = []

    #1
    def __init__(self,user_name,password,full_name,email):

        """
        Class that generates new instances of users.
        """

        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.email = email

    #2
    def save_user(self):

        '''
        save_user method saves users objects into user_list
        '''

        User.user_list.append(self)


    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def user_exist(cls,username,password):
        '''
        Method that checks if a contact exists from the user list.
        '''
        for user in cls.user_list:
            if user.user_name == username and user.password == password:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list saved
        '''
        return cls.user_list


 # Class for all Credentials
class Credentials:
    '''
    Class that generates new instances of Credentials accounts.
    '''
    #Empty Credentials list
    accounts = []
    @classmethod
    def check_user(cls,full_name,password):
        '''
        Method that checks if name and password entered match entries in the user_list
        '''
        current_user=''
        for user in User.user_list:
            if(user.full_name == full_name and user.password == password):
                current_user = user.full_name
                return current_user

    def __init__(self,account_name,user_account,account_password):
        '''
        Class that generates new instances of users.
        '''
        self.account_name = account_name
        self.user_account = user_account
        self.account_password = account_password

    def save_account(self):
        '''
        save_user method saves users objects into user_list
        '''

        Credentials.accounts.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account
        '''

        Credentials.accounts.remove(self)
    
    @classmethod
    def account_exist(cls,email):
        '''
        Method that checks if a contact exists from the user list.
        Args:
            number: Email to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.accounts:
            if account.user_account == email:
                    return True

        return False


    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.accounts
