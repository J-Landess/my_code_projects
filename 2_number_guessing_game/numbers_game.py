import random

def run():
    while True:
        number = random.randint(1,100)
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))  
            if user_guess < number:
                print("guess higher")
            elif user_guess > number:
                print("guess lower")
            else:
                print("You guessed it!!")            
                break
        except ValueError:
            print("Value error!!! Please enter an integer")    
            
run()           