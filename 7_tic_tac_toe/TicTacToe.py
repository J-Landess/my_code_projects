import numpy as np

player_1 = "X"
player_2 = "O"

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board(board):
    print('---+---+---')
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]} ')
        print('---+---+---')

def get_move(player, board):
    while True:
        try:
            print(f"It is {player}'s turn")
            row = int(input("Please select a row 0-2: "))
            column = int(input("Please enter a column 0-2: "))
            if board[row][column] == " ":
                board[row][column] = player
                print_board(board)
                break
            else:
                print("That spot is taken")    
        except ValueError:
            print("Invalid entry. Please enter numbers for row and column.")
        except IndexError:
            print("Invalid entry. Please choose row and column between 0 and 2.")

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_draw(board):
    for row in board:
        for spot in row:
            if spot == " ":
                return False
    return True

def run_game():
    current_player = player_1  # Start with player 1
    while True:
        get_move(current_player, board)
        
        # Check if the current player won
        if check_winner(board):
            print(f"Congratulations, {current_player}! You win!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print("It's a draw! No one wins.")
            break
        
        # Switch players
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1

# Run the game
run_game()






# import numpy as np
# player = ["player_1", "player_2"]
# player_1 = "X"
# player_2 = "O"

# board = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
#     ]
# def print_board(board):
#     print('---+---+---')
#     for row in board:
#         print(f' {row[0]} | {row[1]} | {row[2]} ')
#         print('---+---+---')

# def get_move(player, board):
#     while True:
        
#         try:
#             print(f"It is {player}'s turn")
#             row = int(input("Please select a row 0-2: "))
#             column = int(input("Please enter a column 0-2: "))
#             if board[row][column] == " ":
#                 board[row][column] = player
#                 print_board(board)
#                 break
#             else:
#                 print("That spot is taken")    
#         except ValueError:
#             print("Invalid entry")
#         break

# def check_winner(board):
    
#     for i in range(3):
#         # up and down side to side
#         if board[i][0] == board[i][1] == board[i][2] != " ":
#             return True
#         if board[0][i] == board[1][i] == board[2][i] != " ":
#             return True
#     # Diaganol
#     if board[0][0] == board[1][1] == board[2][2] != " ":
#         return True
#     if board[0][2] == board[1][1] == board[2][0] != " ":
#         return True
#     return False

# def check_draw(board):
#     for row in board:
#         for spot in row:
#             if spot == " ":
#                 return False
#     return True


# def run_game():
#     player = player_1
#     while True:
#         get_move(player_1, board)
#         if check_winner(board):
#             print(f"{player} Wins!!!")
#             break
#         if check_draw(board):
#             print("Game Ties")
#             break

#         if player == player_1:
#             player = player_2
            


# run_game()
# get_move(player_1, board)
# print_board(board)
# get_move(player_2, board)
# print_board(board)


