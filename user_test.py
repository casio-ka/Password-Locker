# Importing the unittest module
import unittest
# Importing the User classes
from user import User
import pyperclip


# Class User Test
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    #1
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        # create user object
        self.new_user = User("casio-ka","password","Wainaina Kasyoka","w_wainaina@hotmail.com")


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"casio-ka")
        self.assertEqual(self.new_user.password,"password")
        self.assertEqual(self.new_user.full_name,"Wainaina Kasyoka")
        self.assertEqual(self.new_user.email,"w_wainaina@hotmail.com")


        #2
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''

         # saving the new user
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

        #3
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("casio-ka","password","Wainaina Kasyoka","w_wainaina@hotmail.com") # new contact
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


        #4
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","Full Name","test@user.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)


    # Test if user exist
    def test_user_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the user.
            '''

            self.new_user.save_user()
            test_user = User("testUser","password","Full Name","test@user.com") # new contact
            test_user.save_user()

            user_exists = User.user_exist("testUser", "password")

            self.assertTrue(user_exists)

    #Display all users
    def test_display_all_users(self):
            '''
            method that returns a list of all contacts saved
            '''

            self.assertEqual(User.display_users(),User.user_list)



if __name__ == '__main__':
    unittest.main()
