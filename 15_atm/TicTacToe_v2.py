from termcolor import colored

player_1 = colored("X","green")
player_2 = colored("O","red")

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
    #Check diagonals
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

def tictactoe():
    current_player = player_1  
    while True:
        get_move(current_player, board)
        if check_winner(board):
            print(f"Congratulations, {current_player}! You win!")
            break
        if check_draw(board):
            print("It's a draw! No one wins.")
            break
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1




