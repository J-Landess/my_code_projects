
import random

players = {
    "player_1": 0,
    "player_2": 0
}

def roll():
    return random.randint(1, 6)

def switch_current_player(current_player):
    return "player_2" if current_player == "player_1" else "player_1"

def check_win(current_player):
    if players[current_player] > 25:
        print(f"{current_player} WINS")
        players["player_1"] = 0
        players["player_2"] = 0
        return True
    return False
 

def run():
    current_player = "player_1" 
    while True:
        print(f"{current_player}'s turn")
        player_roll = roll()
        print(f"{current_player} rolled a {player_roll}")

        if player_roll == 1:
            print(f"You rolled a 1, {current_player} loses all points and it's the other player's turn.")
            players[current_player] = 0
            current_player = switch_current_player(current_player)
            players[current_player] += 0  
        else:
            players[current_player] += player_roll
            print(f"{current_player} now has {players[current_player]} points.")
            check_win(current_player)
            #break
        while True:  
            user_roll = input(f"{current_player} Roll again? (y/n): ").lower()

            if user_roll == "n":
                current_player = switch_current_player(current_player)  
                #print(f"{current_player}'s turn.\n")
                break
            elif user_roll == "y":
                break  
            else:
                print("Invalid option. Please enter 'y' to roll again or 'n' to switch players.")
        
        

run()
