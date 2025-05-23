from atm import user_interface
from collections import Counter
import random
import sys

def print_game():
    char_set = ["💎", "💰", "🍓","💵","👽"]
    game_output = random.choices(char_set,k=3)
    print("|".join(game_output))
    return game_output

def insert_bill():
    credit = 0
    while True:
        try:
            bill = input("Please insert a bill: ")
            credit = int(bill)
            return credit
        except ValueError:
            print("Please insert a positive integer")
           
def place_bet(credit):
    while True:
        try:
            print(f"You have ${credit} credits")
            bet = int(input("How much would you like to bet (1-100): "))
            if bet > 0 and bet < 101 and bet <= credit:
                credit -= bet
                return credit, bet
            else:
                raise ValueError()
        except ValueError:
            print("Enter a correct value")

def payout(game_output, credit, bet):
    counts = Counter(game_output)
    win = 0
    for i in ["💎", "💰", "🍓","💵","👽"]:
        if counts[i] == 3:
            win = bet * 10
            print("YOU WIN 10x")
            credit = win + credit
            print(f"Credit: ${credit}")
            
        if counts[i] == 2:
            win = bet * 2
            print("YOU WIN 2x")
            credit = win + credit
            print(f"Credit: ${credit}")
            
    if credit <= 0:
        while True:
            try:
                play_again = input("your funds are gone...Game over. play again [y/n]: ").lower()
                if play_again == "y":
                    credit = insert_bill()
                    return credit
                elif play_again == "n":
                    print(f"you won ${credit}\nGoodbye ")
                    return None
                else:
                    raise ValueError("Please enter [y/n]")
            except ValueError as e:
                print(e)
    return credit

        
def slot_game():
    credit = insert_bill()
    while credit is not None:
        play_again = input("Play Again?[y/n]: ")
        if play_again.lower() == "no":
            user_interface()
        else:
            credit, bet = place_bet(credit)
            game_output = print_game()
            credit = payout(game_output, credit, bet)

  


