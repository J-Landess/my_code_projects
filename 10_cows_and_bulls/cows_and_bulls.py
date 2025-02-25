import random 
"""
Generate list of 4 random numbers with no numbers the same
while True:
ask user to guess the four numbers
if number in list == number in guess:
    cows += 1
    else:
        bulls += 1
"""

correct_guess = random.sample(range(0, 9), 4)
print(correct_guess[:4])
while True:
    users_guess = int(input("Guess a four digit number, cows are correct number and bulls are incorrect: "))
    bulls = 0
    cows = 0
    if correct_guess[0] == users_guess[0]:
        bulls += 1
        print(f"Bulls: {bulls}")
    elif correct_guess[0] != users_guess[0]:
        cows += 1
        print(f"Cows: {cows}")
    else:
        print("Invalid number")