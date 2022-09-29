
from dbhelpers import conn_exe_close


def login():
   while(True):
        username = input('Please enter the username: ')
        password = input('Please enter the password: ')
        result = conn_exe_close('call login_user(?,?)', [username, password])
        if (len(result) == 1):
            return result
        
        elif (len(result) == 0):
            print('Invalid username/password or user does not exist, Please try again or Sign up')
            ask_user = input('Continue Login? type(yes, y or press enter. To go back type (n, no, or back):  ')
            if (ask_user in ['yes','y','']):
                continue
            elif (ask_user in ['n','no','back']):
                break


def login_signup():
    while(True):
        print('Signup for a new account or login to an existing account')
        print('Option 1 : login to an existing account')
        print('Option 2 : Sign up for a new account')
        user_input = input('press 1 for login or 2 for Sign up:  ')

        if (user_input == '1'):
            print('Enter the already existing username and password')
            result = login()
            if (result):
                print(result)
                return result
            else:
                print('-----------------------')
                continue 

        elif (user_input == '2'):
            print('Enter the username and password for a new user account')
            username = input('Please enter the New username: ')
            password = input('Please enter the New password: ')
            result = conn_exe_close('call add_new_client(?,?)', [username, password])

            if(result):
                print('Congrats you have an account now ', username)
                return result
            elif(not result):
                print('Error Registering', username, ' as a user')
                print('Please try login with correct username/password or Sign up with different username and password')
                print('---------------------------')
                continue


        else:
            print('Not a valid selection, Please select from option 1 or option 2 only.')
            print('--------Please Select from option 1 or 2 only------------')
            continue


user = login_signup()
