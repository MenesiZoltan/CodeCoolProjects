import os
import time

list_of_names = []

def starting():
    os.system("clear")
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" " * 33 + " -----------------------------------------------------------------------------")
    print(" " * 33 + " #######                 #######                      #######" )                
    print(" " * 33 + "    #     #   ####          #       ##     ####          #      ####   ######")
    print(" " * 33 + "    #     #  #    #         #      #  #   #    #         #     #    #  #     ") 
    print(" " * 33 + "    #     #  #              #     #    #  #              #     #    #  ##### ") 
    print(" " * 33 + "    #     #  #              #     ######  #              #     #    #  #     ") 
    print(" " * 33 + "    #     #  #    #         #     #    #  #    #         #     #    #  #     ") 
    print(" " * 33 + "    #     #   ####          #     #    #   ####          #      ####   ######")
    print(" " * 33 + " -----------------------------------------------------------------------------\n")
    time.sleep(3)
    os.system("clear")

def made_by():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" " * 11 + " __  __               _            _                     ______          _   _                __  __           _           ")
    print(" " * 11 + "|  \/  |             | |          | |              _    |___  /         | | (_)     ___      |  \/  |         | |         ")
    print(" " * 11 + "| \  / |   __ _    __| |   ___    | |__    _   _  (_)      / /    ___   | |  _     ( _ )     | \  / |   __ _  | |_    ___ ")
    print(" " * 11 + "| |\/| |  / _` |  / _` |  / _ \   | '_ \  | | | |         / /    / _ \  | | | |    / _ \/\   | |\/| |  / _` | | __|  / _ \ ")
    print(" " * 11 + "| |  | | | (_| | | (_| | |  __/   | |_) | | |_| |  _     / /__  | (_) | | | | |   | (_>  <   | |  | | | (_| | | |_  |  __/")
    print(" " * 11 + "|_|  |_|  \__,_|  \__,_|  \___|   |_.__/   \__, | (_)   /_____|  \___/  |_| |_|    \___/\/   |_|  |_|  \__,_|  \__|  \___|")
    print(" " * 11 + "                                            __/ |                                                                         ")
    print(" " * 11 + "                                           |___/                                                                          ")                                                              
    time.sleep(3)
    os.system("clear")

def user_manual():
    print("\n\n\n\n\n\n\n")
    print("-" * 142)
    print(" " * 65 + "USER MANUAL:\n")
    print(" " * 50 + "1.You will play this game on a 3x3 board.\n")
    print(" " * 27 + "2.You have to choose the numbers between 1 and 9 to be able to enter a correct input.\n")
    print(" " * 15 + "3.The first player who enters his/her name will play with 'X' and the second player is going to play with 'O'.\n")
    print(" " * 63 + "Don\'t cheat! ;)\n")
    print(" " * 58 + "Good luck and have fun! :)")
    print("-" * 142)
    time.sleep(15)
    os.system("clear")
    print(" " * 54 + "This is how the game works.")
    print(" " * 48 + "The sectioning of the numbers look like this.")
    print("\n\n\n\n")
    table_example()
    time.sleep(7)
    os.system("clear")

def table_example():
    print(" " * 58 +"\u250F"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2533"
      +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2533"
      +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2513")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+" " * 7+ "\u2503")
    print(" " * 58 +"\u2503"+ " " * 3 + "7" + " " * 3 + "\u2503"+ " " * 3 + "8" + " " * 3 + "\u2503"+ " " * 3 + "9" + " " * 3 + "\u2503")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503")
    print(" " * 58 +"\u2523"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"
        +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"
        +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u252B")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+" " * 7+ "\u2503")
    print(" " * 58 +"\u2503"+ " " * 3 + "4" + " " * 3 + "\u2503"+ " " * 3 + "5" + " " * 3 + "\u2503"+ " " * 3 + "6" + " " * 3 + "\u2503")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503")
    print(" " * 58 +"\u2523"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"
        +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"
        +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u252B")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+" " * 7+ "\u2503")
    print(" " * 58 +"\u2503"+ " " * 3 + "1" + " " * 3 + "\u2503"+ " " * 3 + "2" + " " * 3 + "\u2503"+ " " * 3 + "3" + " " * 3 + "\u2503")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503")
    print(" " * 58 +"\u2517"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u253B"
        +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u253B"
        +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u251B")         

def thanking():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" " * 5 + " _____   _                    _                              __                        _                 _                 _     _  __  ")
    print(" " * 5 + "|_   _| | |_    __ _   _ _   | |__    _  _   ___   _  _     / _|  ___   _ _     _ __  | |  __ _   _  _  (_)  _ _    __ _  | |   (_) \ \ ")
    print(" " * 5 + "  | |   | ' \  / _` | | ' \  | / /   | || | / _ \ | || |   |  _| / _ \ | '_|   | '_ \ | | / _` | | || | | | | ' \  / _` | |_|    _   | |")
    print(" " * 5 + "  |_|   |_||_| \__,_| |_||_| |_\_\    \_, | \___/  \_,_|   |_|   \___/ |_|     | .__/ |_| \__,_|  \_, | |_| |_||_| \__, | (_)   (_)  | |")
    print(" " * 5 + "                                      |__/                                     |_|                |__/             |___/            /_/ ")
    time.sleep(4)
    os.system("clear")

def restart_screen():
    print("\n\n\n")
    print(" " * 6 + "  _    _                _      _                         _  _  _            _                             _                 _    ___  ") 
    print(" " * 6 + " | |  | |              | |    | |                       | |(_)| |          | |                           | |               | |  |__ \ ")
    print(" " * 6 + " | |  | |  ___   _   _ | |  __| |  _   _   ___   _   _  | | _ | | __  ___  | |_   ___    _ __   ___  ___ | |_   __ _  _ __ | |_    ) |")
    print(" " * 6 + " | |/\| | / _ \ | | | || | / _` | | | | | / _ \ | | | | | || || |/ / / _ \ | __| / _ \  | '__| / _ \/ __|| __| / _` || '__|| __|  / / ")
    print(" " * 6 + " \  /\  /| (_) || |_| || || (_| | | |_| || (_) || |_| | | || ||   < |  __/ | |_ | (_) | | |   |  __/\__ \| |_ | (_| || |   | |_  |_|  ")
    print(" " * 6 + "  \/  \/  \___/  \__,_||_| \__,_|  \__, | \___/  \__,_| |_||_||_|\_\ \___|  \__| \___/  |_|    \___||___/ \__| \__,_||_|    \__| (_)  ")
    print(" " * 6 + "                                    __/ |                                                                                             ")
    print(" " * 6 + "                                   |___/                                                                                              ")
    print("\n\n\n")
    print(" " * 25 + " ___                                 _  _           _  _           ___                           ")                           
    print(" " * 25 + "(  _`\                              ( )( )         ( )( )     _  /'___)                          ")                          
    print(" " * 25 + "| |_) ) _ __    __    ___   ___     (_)(_)  _   _  (_)(_)    (_)| (__      _   _    __    ___    ")   
    print(" " * 25 + "| ,__/'( '__) /'__`\/',__)/',__)           ( ) ( )           | || ,__)    ( ) ( ) /'__`\/',__)   ") 
    print(" " * 25 + "| |    | |   (  ___/\__, \\__, \            | (_) |           | || |       | (_) |(  ___/\__, \ _ ")
    print(" " * 25 + "(_)    (_)   `\____)(____/(____/           `\__, |           (_)(_)       `\__, |`\____)(____/(_)")
    print(" " * 25 + "                                           ( )_| |                        ( )_| |                ")
    print(" " * 25 + "                                           `\___/'                        `\___/'                ")
    print(" " * 25 + " ___                                 _  _           _  _           ___                           ")  
    print(" " * 25 + "(  _`\                              ( )( )         ( )( )     _  /'___)                          ")
    print(" " * 25 + "| |_) ) _ __    __    ___   ___     (_)(_)   ___   (_)(_)    (_)| (__       ___     _            ")
    print(" " * 25 + "| ,__/'( '__) /'__`\/',__)/',__)           /' _ `\           | || ,__)    /' _ `\ /'_`\          ")
    print(" " * 25 + "| |    | |   (  ___/\__, \\__, \            | ( ) |           | || |       | ( ) |( (_) ) _          ")
    print(" " * 25 + "(_)    (_)   `\____)(____/(____/           (_) (_)           (_)(_)       (_) (_)`\___/'(_)      ")
    time.sleep(2)

def writing_draw():
    print("\n\n\n\n\n")
    print("    .=-.-.  ,--.--------.   .--.-.     ,-,--.            ,---.                                            ,---.               ,-.-.    .=-.-. ") 
    print("   /==/_ / /==/,  -   , -\ /==/  /   ,-.'-  _\         .--.'  \              _,..---._     .-.,.---.    .--.'  \     ,-..-.-./  \==\  /==/_ / ")
    print("  |==|, |  \==\.-.  - ,-./ \==\ -\  /==/_ ,_.'         \==\-/\ \           /==/,   -  \   /==/  `   \   \==\-/\ \    |, \=/\=|- |==| |==|, |  ")
    print("  |==|  |   `--`\==\- \     \==\- \ \==\  \            /==/-|_\ |          |==|   _   _\ |==|-, .=., |  /==/-|_\ |   |- |/ |/ , /==/ |==|  |  ")
    print("  |==|- |        \==\_ \     `--`-'  \==\ -\           \==\,   - \         |==|  .=.   | |==|   '='  /  \==\,   - \   \, ,     _|==| /==/. /  ")
    print("  |==| ,|        |==|- |             _\==\ ,\          /==/ -   ,|         |==|,|   | -| |==|- ,   .'   /==/ -   ,|   | -  -  , |==| `--`-`   ")
    print("  |==|- |        |==|, |            /==/\/ _ |        /==/-  /\ - \        |==|  '='   / |==|_  . ,'.  /==/-  /\ - \   \  ,  - /==/   .=.     ")
    print("  /==/. /        /==/ -/            \==\ - , /        \==\ _.\=\.-'        |==|-,   _`/  /==/  /\ ,  ) \==\ _.\=\.-'   |-  /\ /==/   :=; :    ")
    print("  `--`-`         `--`--`             `--`---'          `--`                `-.`.____.'   `--`-`--`--'   `--`           `--`  `--`     `=`     ")
    time.sleep(3)
    os.system("clear")

def player_x_winning():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" " * 40 + " __   __    _                                  _           _ ")
    print(" " * 40 + " \ \ / /   | |                                (_)         | |")
    print(" " * 40 + "  \ V /    | |__     __ _   ___    __      __  _   _ __   | |")
    print(" " * 40 + "   > <     | '_ \   / _` | / __|   \ \ /\ / / | | | '_ \  | |")
    print(" " * 40 + "  / . \    | | | | | (_| | \__ \    \ V  V /  | | | | | | |_|")
    print(" " * 40 + " /_/ \_\   |_| |_|  \__,_| |___/     \_/\_/   |_| |_| |_| (_)")
    time.sleep(3)
    os.system("clear")

def player_o_winning():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" " * 40 + "  ____      _                                  _           _ ")
    print(" " * 40 + " / __ \    | |                                (_)         | |")
    print(" " * 40 + "| |  | |   | |__     __ _   ___    __      __  _   _ __   | |")
    print(" " * 40 + "| |  | |   | '_ \   / _` | / __|   \ \ /\ / / | | | '_ \  | |")
    print(" " * 40 + "| |__| |   | | | | | (_| | \__ \    \ V  V /  | | | | | | |_|")
    print(" " * 40 + " \____/    |_| |_|  \__,_| |___/     \_/\_/   |_| |_| |_| (_)")    
    time.sleep(3)
    os.system("clear")

def congratulations():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" " * 27 + "   ___                                    _           _         _    _                         _")
    print(" " * 27 + "  / __\  ___   _ __    __ _  _ __   __ _ | |_  _   _ | |  __ _ | |_ (_)  ___   _ __   ___     / \ ")
    print(" " * 27 + " / /    / _ \ | '_ \  / _` || '__| / _` || __|| | | || | / _` || __|| | / _ \ | '_ \ / __|   /  / ")
    print(" " * 27 + "/ /___ | (_) || | | || (_| || |   | (_| || |_ | |_| || || (_| || |_ | || (_) || | | |\__ \  /\_/ ")
    print(" " * 27 + "\____/  \___/ |_| |_| \__, ||_|    \__,_| \__| \__,_||_| \__,_| \__||_| \___/ |_| |_||___/  \/   ")
    print(" " * 27 + "                      |___/                                                                    ")
    time.sleep(3)
    os.system("clear")

def user_inputs():   
    global list_of_names
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    starting_input_1 = str(input("Please, the first player enter his/her name: "))
    list_of_names.append(starting_input_1)
    os.system("clear") 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    starting_input_2 = str(input("Please, the second player enter his/her name: "))
    list_of_names.append(starting_input_2)
    os.system("clear")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")   
    print(" " * 60 + "-" * len(list_of_names[0] + "-" * len(list_of_names[1] + "-" * 14)))
    print(" " * 60 + "{} = X and {} = O.".format(list_of_names[0], list_of_names[1]))
    print(" " * 60 + "-" * len(list_of_names[0] + "-" * len(list_of_names[1] + "-" * 14)))
    time.sleep(4)
    os.system("clear")



def print_table(): 
    print("\n\n\n\n\n\n\n")
    print(" " * 58 +"\u250F"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2533"
      +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2533"
      +"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2513")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+" " * 7+ "\u2503")
    print(" " * 58 +"\u2503"+ " " * 3 + row1[0] + " " * 3 + "\u2503"+ " " * 3 + row1[1] + " " * 3 + "\u2503"
        + " " * 3 + row1[2] + " " * 3 + "\u2503")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503")
    print(" " * 58 +"\u2523"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"+
        "\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"+
        "\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u252B")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+" " * 7+ "\u2503")
    print(" " * 58 +"\u2503"+ " " * 3 + row2[0] + " " * 3 + "\u2503"+ " " * 3 + row2[1] + " " * 3 + "\u2503"
        + " " * 3 + row2[2] + " " * 3 + "\u2503")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503")
    print(" " * 58 +"\u2523"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"+
        "\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u254B"+
        "\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u252B")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+" " * 7+ "\u2503")
    print(" " * 58 +"\u2503"+ " " * 3 + row3[0] + " " * 3 + "\u2503"+ " " * 3 + row3[1] + " " * 3 + "\u2503"
        + " " * 3 + row3[2] + " " * 3 + "\u2503")
    print(" " * 58 +"\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503"+ " " * 7+ "\u2503")
    print(" " * 58 +"\u2517"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u253B"+
        "\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u253B"+
        "\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u2501"+"\u251B")      

def player_input_to_table():
    tic_tac_toe_table.pop(int(place_mark) - 1)
    tic_tac_toe_table.insert(int(place_mark) - 1, x_or_o_variable)

def wining_conditionss():
    if tic_tac_toe_table[0] == tic_tac_toe_table[1] and tic_tac_toe_table[0] == tic_tac_toe_table[2] and not "_" or\
    tic_tac_toe_table[3] == tic_tac_toe_table[4] and tic_tac_toe_table[3] == tic_tac_toe_table[5] and not "_" or\
    tic_tac_toe_table[6] == tic_tac_toe_table[7] and tic_tac_toe_table[6] == tic_tac_toe_table[8] and not "_" or\
    tic_tac_toe_table[0] == tic_tac_toe_table[5] and tic_tac_toe_table[0] == tic_tac_toe_table[8] and not "_" or\
    tic_tac_toe_table[2] == tic_tac_toe_table[5] and tic_tac_toe_table[2] == tic_tac_toe_table[6] and not "_":
        return True

def draw_game_restart_or_exit():
    if len(list_of_player_inputs) == 9:
        return True

def clear_game_for_restart():
    player_input.clear()
    global tic_tac_toe_table
    tic_tac_toe_table = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    global x_or_o_variable
    x_or_o_variable = "X"

def boot_game():
    starting()
    made_by()
    user_manual()
    user_inputs()

def x_or_o_counter():
    if len(list_of_player_inputs) %2 == 0 or len(player_input) == 0:
        global x_or_o_counter
        x_or_o_counter = "X"
    if len(list_of_player_inputs) %2 != 0
        global x_or_o_counter
        x_or_o_counter = "O"



tic_tac_toe_table = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
list_of_player_inputs = []
possible_player_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
possible_player_inputs_for_restart = ["y", "n"]
x_or_o_variable = X

boot_game()

print_table()

while True:
    place_mark = input("Player please enter coordinate: ")
    if place_mark not in possible_player_inputs:
        print("Invalid input. Enter valid input.")
        place_mark = input("Player please enter coordinate: ")
    while place_mark in player_input:
        print("Place already taken. Please choose another one.")
        place_mark = input("Player please enter coordinate: ")
    os.system("clear")
    player_input.append(place_mark)
    input_possibilities()
    print_table()
    wining_conditions()
    if wining_conditions() == True:
        os.system("clear")
        player_x_winning()
        congratulations()
        restart_screen()
        print("\n\n\n\n\n\n\n\n\n")
        restart = input(" " * 67 + "y / n:")
        while restart not in possible_player_inputs_for_restart:
            print("Invalid input. Please enter y or n (case sensitive).")
            restart = input("y / n: ")
        os.system("clear")
        if restart == "y":
            clear_game_for_restart()
            print_table()
            continue
        elif restart == "n":
            break
    if draw_game_restart_or_exit() == True:
        writing_draw()
        draw_restart = input("y / n: ")
        while draw_restart not in possible_player_inputs_for_restart:
            print("Invalid input. Please enter Y or N (case sensitive).")
            draw_restart = input("y / n: ")
        if draw_restart == "y":
            clear_game_for_restart()
            print_table()
            continue
        elif draw_restart == "n":
            break      

thanking()