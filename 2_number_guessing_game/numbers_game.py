import random

number = random.randint(1,100)
while True:
    try:
        user_guess = input("Guess a number between 1 and 100: ")   
        if int(user_guess) < number:
            print("guess higher")
        elif int(user_guess) > number:
            print("guess lower")
        else:
            print("You guessed it!!")            
            break
    except ValueError:
        print("Value error!!! Please enter an integer")    
        
        