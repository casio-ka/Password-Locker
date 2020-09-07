# Importing the unittest module
import unittest
# Importing the Credential class
from user import Credentials
import pyperclip



class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    #1
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        # create user object
        self.new_account = Credentials("WhatsApp","daudi","password")


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.accounts = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.user_account_name,"WhatsApp")
        self.assertEqual(self.new_account.user_account_user,"daudi")
        self.assertEqual(self.new_account.user_account_password,"password")


    def test_save_account(self):
        '''
        test_save_user test case to test if the credential object is saved into
        the account list
        '''

        # saving the new credential account
        self.new_account.save_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_accounts to check if we can save multiple accounts
        objects to our accounts
        '''
        self.new_account.save_account()
        test_account = Credentials("WhatsApp","daudi","password") # new account
        test_account.save_account()
        self.assertEqual(len(Credentials.accounts),2)

    def test_delete_account(self):
            '''
            test_delete_user to test if we can remove a account from our accounts
            '''
            self.new_account.save_account()
            test_account = Credentials("Test","user","password") # new account
            test_account.save_account()

            self.new_account.accounts

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(Credentials.accounts),1)



    def test_find_account_by_number(self):
            '''
            test to check if we can find a account by phone number and display information
            '''

            self.new_account.save_account()
            test_account = Credentials("Test","anum","password") # new account
            test_account.save_account()

            found_account = Credentials.find_by_number("anum")

            self.assertEqual(found_account,Credentials.find_by_number("anum"))



    # Test if account exist
    def test_account_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the user.
            '''

            self.new_account.save_account()
            test_account = Credentials("Viber","daudi","12345") # new account
            test_account.save_account()

            account_exists = Credentials.account_exist("daudi")

            self.assertTrue(account_exists)

    """
    Dispaly account user
    """
    def test_display_all_account(self):
            '''
            method that returns a list of all account saved
            '''

            self.assertEqual(Credentials.display_accounts(),Credentials.accounts)


if __name__ == '__main__':
    unittest.main()
