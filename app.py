from random import *
import secrets
# importing helpers from module to use in app.py
from operator import indexOf, truediv
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


# client_result = login_signup()
# client_id = client_result[0][0]
# client_name = client_result[0][1]
# # print(client_id)
# print(client[0][0], client[0][1].decode('utf-8'))
# ---------------------------------------------------------------------------------------------------------------

# all moves will show all the moves available
def all_moves():

    results = conn_exe_close('call all_moves()',[])
    if(results):
        return results

# show fighters and create fighter and choose fighter is started here
# ---------------------------------------------------------------------------------------------------------------------
# fighters of client will return all the fighters associated with particular client
def fighters_of_client(client_id):
    result = conn_exe_close('call fighters_of_client(?)',[client_id])
    # if there is any client it will return the function
    if(len(result) != 0):
        return result
        # if no fighter then it will just print the message
    elif(len(result) == 0):
        print('No fighter exists for ')
        print('---------------------------------------------------')

# check list will compare parent list with child list
# it will check for every item in child list exists in parent list
# if everything is included then it will not execute the false return
# after looping and the statements stays false it will return true
def check_lists(parent_list,child_list):
    for item in child_list:
        if item not in parent_list:
            return False
            
    return True

# create a fighter will create a fighter with given client id
def create_fighter(client_id):
    while(True):
        print('Please add the name and 4 moves for fighter')
        # ask for input the name of a new fighter
        name = input('Enter the name for your fighter:  ')
        # will bring all the moves from all moves function
        results =  all_moves()
        # print all the moves got from all_moves()
        available_moves = []
        for result in results:
            available_moves.append(result[0])
            print('Move ID:',result[0],' ',result[1].decode('utf-8'))
            print('Lower Damage Range: ', result[2].decode('utf-8'))
            print('Upper Damage Range: ', result[3].decode('utf-8'))
            print('--------------------------------')
        print('Please pick any of the 4 moves from the above by typing their move number')
        # ask the user for 4 inputs for the moves
        while(True):
            move_one = input('Enter Number 1: ')
            move_two = input('Enter number 2: ')
            move_three = input('Enter number 3: ')
            move_four = input('Enter number 4: ')
            moves = [move_one,move_two,move_three,move_four]
            moves_int = []
            try:
                for move in moves:
                    move = int(move)
                    moves_int.append(move)
                    # check if moves are valid and from one of the option available
                    compare_moves = check_lists(available_moves,moves_int)
                    if(compare_moves == True):
                        # after getting the name and moves a fighter create stores procedure will get called 
                        # it will take 6 arguments in total
                        added_fighter = conn_exe_close('call create_fighter(?,?,?,?,?,?)',[name,client_id,move_one,move_two,move_three,move_four])
                        print('fighter is added')
                        return added_fighter
                    # if fighter add is successful then statement is printed and function will be returned
                    
                    elif(compare_moves == False):
                        # if not then function will continue asking for the correct inputs
                        print('Please enter the correct id from the below list of move id(s)')
                        print(available_moves)
                        print('--------------------------------------------------------')
            except ValueError as error:
                print('Value Error:', error)
                print('Please enter valid integer')
            

# pick create fighter will use both create_fighter and fighters_of_client()
# based on conditions it will execute one of these function
def pick_create_fighter(client_id):
    while(True):
        print('Please pick a fighter or create a new fighter')
        print('Option 1 to pick an existing fighter...')
        print('Option 2 to create a new fighter..')
        # to start it will ask the user to input 1 or 2
        user_input = input('Please enter option 1 or 2 :  ')
        # if user entered 1 then it will execute fighters of client 
        # and show all the fighters related to the client
        if(user_input == '1'):
            while(True):
                print('The list of available fighters')
                results = fighters_of_client(client_id)
                if(results):
                    # fighters_available will store the fighters id to compare with something
                    fighters_available = []
                    for result in results:
                        # appending the id of a fighter to the list 
                        fighters_available.append(result[0]) 
                        # print the available fighters id and name decoded
                        print('Fighter ID:',result[0],': ',result[1].decode('utf-8'))
                        print('-----------------------------------------------------')
                    while(True):
                        try:
                            # ask the user to input the fighter id
                            choose_fighter = input('Please enter the fighter id: ')
                            # if chosen fighter is available then it will return the function with chosen fighter id
                            # convert the fighter id to int because database accepts int for id
                            choose_fighter = int(choose_fighter)
                            if (choose_fighter in fighters_available):
                                return choose_fighter
                                # if chosen fighter is not available then the msg is printed and the function continued
                            elif(choose_fighter not in fighters_available):
                                print('Please enter a valid number for a fighter ID from the list of fighters')
                                print('List of available fighters')
                                print(fighters_available)
                                print('---------------------------------------------')
                        except ValueError as error:
                            print('Please enter number only')
                            print('Value Error: ', error)
                # if not fighter exists for a client then go back and ask for the fighter to create 
                # with a name and four moves
                elif(not results):
                    print('please create a new fighter by choosing option 2')
                    print('---------------------------------------')
                    break
                    
        # if user input is 2 when selecting the options in starting
        # then user will be asked to create a fighter with name and four moves
        elif(user_input == '2'):
            result = create_fighter(client_id)
            if(result):
                fighter_id =  result[0][0]
                return fighter_id
        # if user entered something else instead of 1 or 2 then user will sent back to starting
        # and asked again to choose option 1 or 2..
        else:
            print('Please select option 1 or 2 ')
            print('------------------------')

# fighter_id =  pick_create_fighter(client_id)

# show opponent and choose opponent starts here
#----------------------------------------------------------------------------------------
# to show all the computer fighters
def show_opponent():
    results = conn_exe_close('call computer_fighters()',[])
    return results

# choose the computer fighter
def choose_opponent():
    print('choose the available opponent:')
    # it will call the show opponent to get opponents and then print
    opponents = show_opponent()
    opponents_available = []
    if(opponents):
        # print all the opponents 
        for opponent in opponents:
            opponents_available.append(opponent[0])
            print('opponent ID:',opponent[0],'Name:',opponent[1].decode('utf-8'),'Health: ',opponent[2])
        # ask for input for the opponent
        while(True):
            selected_opponent = input('To select the opponent,Enter the Opponent ID: ')
            selected_opponent = int(selected_opponent)
            if(selected_opponent in opponents_available):
                return selected_opponent
            else:
                print('Error: Invalid opponent id entered')
                print('Please choose one of the opponents from the list')
                print(opponents_available)
                

# opponent_id = choose_opponent()

# difficulty and points starts here
# ---------------------------------------------------------------------------------------------------------------
# diffculty level 1,2 and 3
def difficulty_level():
    print('Select the opponent difficulty')
    print('1: weak opponent')
    print('2: fair opponent')
    print('3: strong opponent')
    diff = input('please enter the difficulty number: ')
    # user can choose option from 1 to 3 if else than it will ask 
    while(True):
        diff = int(diff)
        if(diff >=1 and diff <= 3):
            return diff
        elif(diff <= 0 or diff >= 4):
            continue

# points user depend upon difficulty level
def points_user(diff):
    if(diff == 1):
        return 1
    elif(diff == 2):
        return 2
    elif(diff == 3):
        return 4
    else:
        print('difficulty level not selected, so by default it will be weaker opponent')
        return 1       

# grace user will take difficulty level and fighter id
# to produce points and update them to the database for the specific fighter
def grace_user(winner,diff_level,fighter_id):
    if(winner == 'user'):
        points = points_user(diff_level)
        total_points = conn_exe_close('call update_user_points(?,?)',[fighter_id,points])
        return total_points

# user_score =  diff_level()
# grace_user(user_score,fighter_id)

# if difficulty level is week user will get the 10 extra health points after attack from computer
# if level is 2 then extra 5 health points will get deducted from fighters health
# if level is 3 then extra 10 health points will get deducted from health of fighter
def grace_opponent(fighter_id,diff_level):
    fighter_health = conn_exe_close('call health_user_before(?)',[fighter_id])
    original_health = fighter_health[0][0]
    if(diff_level == 1):
        new_health = original_health + 10
        updated_health_db = conn_exe_close('call health_user_after(?,?)',[fighter_id, new_health])
        return updated_health_db[0][0]
    elif(diff_level == 2):
        new_health = original_health - 5
        updated_health_db = conn_exe_close('call health_user_after(?,?)',[fighter_id, new_health])        
        return updated_health_db[0][0]
    elif(diff_level == 3):
        new_health = original_health - 10
        updated_health_db = conn_exe_close('call health_user_after(?,?)',[fighter_id, new_health])        
        return updated_health_db[0][0]


# user moves section starts here
# ------------------------------------------------------------------------------------------------------------ 
# this function will display all moves of the fighter
def fighter_moves(fighter_id):
    moves = conn_exe_close('call fighter_moves(?)',[fighter_id])
    return moves
# this function will get used in getting the details about specific move 
# for example lower and upper range of a given move id
def specific_move(move_id):
    result = conn_exe_close('call specific_move(?)',[move_id])
    return result

# pick moves will help pick and input moves for the attack on the opponent
def pick_move(fighter_id):
    # will call fighters move to bring all the moves from th database
    # associated with the specific fighter
    moves = fighter_moves(fighter_id)
    print('All the available moves for your fighter')
    # use the list to store all moves to compare
    moves_available = []
    # print all the moves after getting from fighter moves function
    for move in moves:
        print('move ID:',move[0],' move Name:',move[1].decode('utf-8'))
        print('Lower damage range:',move[2].decode('utf-8'),' Upper damage range:',move[3].decode('utf-8'))
        print('-------------------------------------------------')
        # will append all the move ids into moves available
        moves_available.append(move[0])
    while(True):
        # will run a while loop until correct move from the available moves is not entered
        move_input = input('Please enter the move ID to attack: ')
        move_input = int(move_input)
        if(move_input in moves_available):
            # if valid move is entered from the list 
            return move_input
        elif(move_input not in moves_available):
            # if not valid move is entered from the list
            print('Please select the valid move from moves available for this fighter')
            print(moves_available)
            continue

# ---------------------------------------------------------------------------------------------------------------
# return opponent moves with the id of opponent
def opponent_moves(opponent_id):
    moves = conn_exe_close('call opponent_moves(?)',[opponent_id])
    return moves
# returns random move number from available moves for the selected opponent
def opponent_random_selected_move(list):
    random_number = secrets.choice(list)
    return random_number
# selecting the move for opponent with the help of two functions
# opponent moves and opponent random selected move
def opponent_pick_move(opponent_id):
    moves = opponent_moves(opponent_id)
    moves_available = []
    for move in moves:
        moves_available.append(move[0])
        print('move ID:',move[0],' move Name:',move[1].decode('utf-8'))
        print('Lower damage range:',move[2].decode('utf-8'),' Upper damage range:',move[3].decode('utf-8'))
        print('-------------------------------------------------')
    random_number = opponent_random_selected_move(moves_available)
    move_selected = random_number
    return move_selected

# opponent_pick_move(opponent_id)

# random damage by player will return the random number 
# from the lower and upper range of move selected by player or user
# it will use the pick move and specific move funciton to 
# grab all the move and then use that move id to get details about that move
# for example upper and lower damage range of that move
def random_damage_number_by_player(fighter_id):
    while(True):
        move = pick_move(fighter_id)
        move_values = specific_move(move)
        # after getting the moves will store the upper and lower damage 
        # range and store both values in different variables
        # just because to use them create a random number between those two values
        # and this function will return the random number by user fighter
        if(move_values):
            value_one = int(move_values[0][0].decode('utf-8'))
            value_two = int(move_values[0][1].decode('utf-8'))
            random_number = randint(value_one, value_two)
            return random_number
# health of the opponent before the attack or every attack
# this function will return the present health from the database
def health_opponent_before(opponent_id):
    health = conn_exe_close('call health_opponent_before(?)',[opponent_id])
    return health

# this function eill update the opponent health
# with the help of two arguments opponent id and oppeonent new health 
# it will get opponent new health after substracting the damage from original health
def health_opponent_after(opponent_id, new_health_opponent):
    health = conn_exe_close('call health_opponent_after(?,?)',[opponent_id, new_health_opponent])
    return health

# damage to opponent will use 
# random_damage number by opponent, health opponent before and
# health opponent after just to  view the old health , do damage and
# update the health of an opponent
def damage_to_opponent(fighter_id,opponent_id):
    damage = random_damage_number_by_player(fighter_id)
    health_before = health_opponent_before(opponent_id)
    new_health_opponent = health_before[0][0] - damage
    health_after = health_opponent_after(opponent_id,new_health_opponent )
    return health_after[0][0]


# new_health_opponent = damage_to_opponent(fighter_id,opponent_id)

# random number generated by opponent from lower and upper
# range of its selected move
def random_damage_number_by_opponent(opponent_id):
    # first it will pick move
    random_move = opponent_pick_move(opponent_id)
    # seconf it will get that move and get its lower and upper range
    move_values = specific_move(random_move)
    if(move_values):
        # if values come back then decode them to convert them into integers for random function
        value_one = int(move_values[0][0].decode('utf-8'))
        value_two = int(move_values[0][1].decode('utf-8'))
        random_number = randint(value_one, value_two)
        # return the random number between two values 
        return random_number

# health user will return the health of a user befor or every attack
def health_user_before(fighter_id):
    health = conn_exe_close('call health_user_before(?)',[fighter_id])
    return health
# health user after will update the new health to the database and return the new health
def health_user_after(fighter_id, new_health_fighter):
    health_after = conn_exe_close('call health_user_after(?,?)',[fighter_id, new_health_fighter])
    return health_after


# damage to user will get done by opponent 
# will generete random number 
# look at health and subtract the damage from health
def damage_to_user(opponent_id, fighter_id):
    damage = random_damage_number_by_opponent(opponent_id)
    health_before = health_user_before(fighter_id)
    new_health = health_before[0][0] - damage
    health_after = health_user_after(fighter_id, new_health)
    return health_after[0][0]

def check_winner(health_opponent, health_user):
    if(health_opponent > health_user):
        print('Opponent has won this turn')
        return 'opponent'
    elif(health_user > health_opponent):
        print('User has won this turn')
        return 'user'


def play_game():
    client_result = login_signup()
    client_id = client_result[0][0]
    client_name = client_result[0][1]
    fighter_id =  pick_create_fighter(client_id)
    opponent_id = choose_opponent()
    diff_level = difficulty_level()
    health_opponent = damage_to_opponent(fighter_id,opponent_id)
    damage_to_user(opponent_id,fighter_id)
    health_user = grace_opponent(fighter_id,diff_level)
    winner = check_winner(health_opponent,health_user)
    points_user_fighter = grace_user(winner,diff_level,fighter_id)
    print('Points for',client_name,':', points_user_fighter)

play_game()

