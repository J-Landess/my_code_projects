import random
import sys
players = {
    "player_1": [0,"_"],
    "player_2": [0,"_"]
    } 
def get_name():
    first_player_name = input("\nplayer one what is your name: ")
    players["player_1"][1] = first_player_name
    second_player_name = input("\nplayer two what is your name: ")
    players["player_2"][1] = second_player_name
    return players
def roll():
    return random.randint(1, 6)

def switch_current_player(current_player):
    if current_player == "player_1":
        current_player = "player_2"
    else:
        current_player = "player_1"
    return current_player

def check_win(current_player):
    if players[current_player][0] > 25:
        print(f"\n{players[current_player][1]} WINS")
        play_again = input("\nPlay again? [y/n]: ")
        if play_again.lower() == "n":
            sys.exit()
        else:
            players["player_1"][0] = 0
            players["player_2"][0] = 0
            run()
        return True
    return False
 

def run():
    print("\nwelcome to the pig dice game")
    get_name()
    # name_1 = players["player_1"][1] 
    # name_2 = players["player_2"][1]
    current_player = "player_1" 
    while True:
        print(f"\n{players[current_player][1]}'s turn")
        player_roll = roll()
        print(f"\n{players[current_player][1]} rolled a {player_roll}")

        if player_roll == 1:
            print(f"\nYou rolled a 1, \n{players[current_player][1]} loses all points and it's the other player's turn.")
            players[current_player][0] = 0
            current_player = switch_current_player(current_player)
            players[current_player][0] += 0  
        else:
            players[current_player][0] += player_roll
            print(f"\n{players[current_player][1]} now has {players[current_player][0]} points.")
            if check_win(current_player):
                sys.exit()
                
        while True:  
            user_roll = input(f"{players[current_player][1]} Roll? (y/n): ").lower()

            if user_roll == "n":
                current_player = switch_current_player(current_player)  
                #print(f"{current_player}'s turn.\n")
                break
            elif user_roll == "y":
                break  
            else:
                print("Invalid option. Please enter 'y' to roll again or 'n' to switch players.")
        
        

run()
