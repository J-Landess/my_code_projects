import random



ROCK = "r"
PAPER = "p"
SCISSORS = "s"
choices = (ROCK, PAPER, SCISSORS)


while True:
    try:
        user_choice = input("Rock, Paper, or Scissors [r/p/s]: ")
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            print(f"Computer chose: {computer_choice.upper()}..You tied!")
            if input("play again [y/n]") == "n":
                break
        
        elif (user_choice == ROCK and computer_choice == PAPER) or (user_choice == PAPER and computer_choice == SCISSORS) or (user_choice == SCISSORS and computer_choice == ROCK):
            print(f"Computer chose: {computer_choice.upper()}..You Lose!")
            if input("play again [y/n]") == "n":
                break
        elif (user_choice == ROCK and computer_choice == SCISSORS) or (user_choice == SCISSORS and computer_choice == PAPER) or (user_choice == PAPER and computer_choice == ROCK):
            print(f"Computer chose: {computer_choice.upper()}..You Win!")
            if input("play again [y/n]") == "n":
                break
        else:
            print("Invalid Choice")
            if input("play again [y/n]") == "n":
                print("Thanks for playing")
                break
            

    except ValueError:
        print("Invalid Choice")



