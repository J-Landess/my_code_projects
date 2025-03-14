import random

def get_word():
    word_list = ["computer","dog","couch","back","spanish"]
    random_word = random.choice(word_list)
    
    return random_word



def get_user_guess():
    while True:
        try:
            user_guess = input("Please enter a letter: ")
            if not user_guess.isalpha():
                raise ValueError("Invalid!! Please enter a letter: ")
            if len(user_guess) != 1:
                raise ValueError("Ivalid!! Please enter only one letter: ")
            return user_guess
        except ValueError as e:
            print(e)


def run():
    guessed_letters = set()
    word = get_word()
    print(f"{word}")
    attempts = 6
    while attempts > 0:
        user_guess = get_user_guess().lower()
        if user_guess in guessed_letters:
            print("You already guessed this")
        else:
            guessed_letters.add(user_guess)
        if user_guess in word:
            print(f"{user_guess} is Correct")
            
            continue
        else:
            print(f"{user_guess} is incorrect")
            attempts -= 1
            print(f"You have {attempts} trys left")
run()    