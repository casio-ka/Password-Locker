#!/usr/bin/env python3.8
from user import User
from user import Credentials
import getpass
import os
import shutil
import string
import random
os.system('setterm -background white -foreground black -store')

def create_user(user_name,password,full_name,email):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password,full_name,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(email):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_email(email)

def check_existing_users(username,userpassword):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(username,userpassword)


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

# Credentials

def create_account(account_name,user_account,account_password):
    '''
    Function to create a new account
    '''
    new_account= Credentials(account_name,user_account,account_password)
    return new_account

def save_accounts(account):
        '''
        Function to save account credential
        '''
        account.save_account()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()

def id_generator(size=11, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def find_account(name):
    '''
    Function that finds a user by name and returns the account
    '''
    return Credentials.find_by_number(name)

def del_account(account):
    '''
    Function to delete a account
    '''
    account.account_dele()


# MAIN FUNCTION

def main():
        print("Thanks for Using Password Locker App.")

while True:

    columns = shutil.get_terminal_size().columns
    print("WELCOME TO:".center(columns))
    print("PASSWORD LOCKER".center(columns))
    print("-"*100)


    print(" Use these codes to navigate: \n Login =(l) \n Create Account=(c) \n Quit - (q)")
    options = input("Enter a choice: ").lower().strip()
    if options == 'q':
        break

    elif options=="c":
        print("Welcome \n")
        print('To create a new account:')
        user_name = input("Enter new UserName : ").strip()
        password = getpass.getpass('Enter your password : ').strip()
        full_name=input("Enter Full Name : ").strip()
        email = input("Enter Email : ")

        print("Thank you for using our service")

        save_users(create_user(user_name,password,full_name,email))
        print('\n')
        print(f"New User {user_name} {full_name} created \n")

        new_login = (user_name + ";" + password + ";" + full_name + ";" + email)

        print(f"Your User info : {new_login}")
        new_login1=new_login.split(";")
        print(new_login1)
        print(new_login1[0])

        """
        Open User File as write and append new authentication
        """

        users_info_file = open("login.txt","a+")
        users_info_file.write("\n"+new_login)
        users_info_file.close()

    elif options == 'l':
        """
        Open User File as read only and append new authentication
        user_get_info_file = open("login.txt","r")
        """
        user_name = input("Enter user name")
        password=getpass.getpass("Enter password")
        found_user = check_existing_users(user_name,password)
        if found_user and password:
            print(" ")
            print(f"Welcome {user_name}. Please choose an option to continue.")
            print(' ')
            while True:
                print("-"*100)
                print('Navigation Codes: \n New Credential - (n) \n Display Credentials -(d) \n Exit -(e) ')
                options = input("Enter a choice: ").lower().strip()
                print("-"*100)
                if options == 'e':
                    print(" ")
                    print(f'Goodbye {user_name}')
                    break
                elif options == 'n':
                    print(' ')
                    print('Enter your Credential Details:')
                    account_name = input("Enter application\'s name : ").strip()
                    user_account=input("Enter you account\'s name : ").strip()
                    while True:
                        print(' ')
                        print("-"*100)
                        print('Please choose an option for entering a password: \n Enter Existing Password (p) \n Generate Password -(g) \n Exit -(e)')
                        p_choice = input('Enter an option: ').lower().strip()
                        print("-"*100)
                        if p_choice == 'p':
                            print(" ")
                            account_password = getpass.getpass('Enter your password: ').strip()
                            save_accounts(create_account(account_name,user_account,account_password))
                            print(' ')
                            print(f'Credential Created: Account Name: {account_name} - User Account: {user_account} - Password: {account_password}')
                            print(' ')
                            break
                        elif p_choice == 'g':
                            print(" ")
                            print("Generating password for you")
                            autoPassword=id_generator()
                            print("Your new Password Gemereated is: " + autoPassword)
                            save_accounts(create_account(account_name,user_account,autoPassword))
                            print(' ')
                            print(f'Credential Created: Account Name: {account_name} - User Account: {user_account} - Password: {autoPassword}')
                            print(' ')
                            break
                        elif p_choice == 'e':
                            break
                        else:
                            print('Oops! Wrong option entered. Try again.')
                            break
                elif options == 'd':
                    print("Displaying Credential accounts")
                    if display_accounts():
                        print("Here is a list of all your credential accounts")
                        print('\n')
                        for account in display_accounts():
                            print(f"{account.account_name } {account.user_account} .....{account.account_password}")
                            print('\n')
                    else:
                        print(' ')
                        print("You don't seem to have any credentials saved yet")
                        print(' ')
                        break
                else:
                    print ("Invalid Option, Goodbye")


if __name__ == '__main__':

    main()
