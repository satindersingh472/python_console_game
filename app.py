# importing helpers from module to use in app.py
from operator import indexOf
from dbhelpers import conn_exe_close

# wherever the conn_exe_function will get used it will take 2 arguments
# argument 1 is call stored procedure() 
# argument 2 will be list of arguments inside the stored procedure
# argument 2 can be left empty or not even passed to the function 
# and the function will still work 

# login will help take input and return the result if there is a user
# if user does not exist than it will ask to continue
# user can enter the values depending on the condition
def login():
   while(True):
        print('Enter the already existing username and password')
        username = input('Please enter the username: ')
        password = input('Please enter the password: ')
        # conn_exe_close will connect to database , run the stored procedure and close the database
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
# signup will ask for username and password from user to create an account
# if account created is successfull then result is returned
# if not then user will get asked to continue or go back
def signup():
    while(True):
        print('Enter the username and password for a new user account')
        username = input('Please enter the New username: ')
        password = input('Please enter the New password: ')
        # conn_exe_close will connect to database , run the stored procedure and close the database
        result = conn_exe_close('call add_new_client(?,?)', [username, password])
        if (result):
            return result
        else:
            print('Error Registering', username, 'as a new user')
            ask_user = input('Continue Signup? type(yes,y or press enter) To go back type(no,n or back)')
            if(ask_user in ['y','yes','']):
                print('---------------------------')
            elif(ask_user in ['n','no','back']):
                break

 #login_signup will use login and signup functions to ask user for login or signup based on input
 # if user input 1 then login is asked else if 2 is input then signup 
def login_signup():
    while(True):
        print('Signup for a new account or login to an existing account')
        print('Option 1 : login to an existing account')
        print('Option 2 : Sign up for a new account')
        user_input = input('press 1 for login or 2 for Sign up:  ')
        if (user_input == '1'):
            result = login()
            if (result):
                print('Welcome back ',result[0][1])
                print('Your user ID is: ',result[0][0])
                return result
            else:
                print('-----------------------')
        elif (user_input == '2'):
            result = signup()
            if(result):
                print('Congrats you have an account now ',result[0][1])
                print('Your user ID is: ',result[0][0])
                return result
            elif(not result):
                print('---------------------------')

        else:
            print('Not a valid selection, Please select from option 1 or option 2 only.')
            print('---------------------------------------------------------')
            print('..Please Select from option 1 or 2 only..')
            print('----------------------------------------------------------')


client_result = login_signup()
client_id = client_result[0][0]
client_name = client_result[0][1]
# print(client_id)
# print(client[0][0], client[0][1].decode('utf-8'))
# ---------------------------------------------------------------------------------------------------------------

def all_moves():
    results = conn_exe_close('call all_moves()',[])
    if(results):
        return results

def fighters_of_client(client_id):
    result = conn_exe_close('call fighters_of_client(?)',[client_id])
    if(len(result) != 0):
        return result
    elif(len(result) == 0):
        print('No fighter exists for ',client_name)

def create_fighter(client_id):
    print('Please add the name and 4 moves for fighter')
    name = input('Enter the name for your fighter:  ')
    results =  all_moves()
    count = 0
    for result in results:
        count += 1
        print(result[1].decode('utf-8'),'  No:', count)
        print('Lower Damage Range: ', result[2].decode('utf-8'))
        print('Upper Damage Range: ', result[3].decode('utf-8'))
        print('--------------------------------')
        while(True):
            print('Please pick any of the 4 moves from the above by typing their move number')
            move_one = input('Enter move number 1: ')
            move_two = input('Enter move number 2: ')
            move_three = input('Enter move number 3: ')
            move_four = input('Enter move number 4: ')
            moves = [move_one,move_two,move_three,move_four]
            for move in moves:
                move = int(move)
                if(move >= 1 and move <= len(results)):
                    added_fighter = conn_exe_close('call create_fighter(?,?,?,?,?,?)',[name,client_id,move_one,move_two,move_three,move_four])
                    return added_fighter
                elif(move <= 0 or move > len(results)):
                    print('Not a valid entry for move')

create_fighter(client_id)

# def pick_create_fighter(client_id):
#     while(True):
#         print('Please pick a fighter or create a new fighter')
#         print('Option 1 to pick an existing fighter...')
#         print('Option 2 to create a new fighter..')
#         user_input = input('Please enter option 1 or 2 :  ')

#         if(user_input == '1'):
#             result = fighters_of_client(client_id)
#             if(result):
#                 return result
#             elif(not result):

