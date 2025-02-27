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

CORRECT_GUESS = random.sample(range(0, 9), 4)
str(CORRECT_GUESS)

print(type(CORRECT_GUESS[:4]))
print(CORRECT_GUESS[:4])
while True:
    cows = 0
    bulls = 0
    try:
        users_guess = [int(i) for i in input("Guess a four digit number: ")]

        print(users_guess)
        print(type(users_guess))
    except ValueError:
        print("Please enter four non repeating numbers: ")
    print("stop")
    for i in range(4):
            if users_guess[i] == CORRECT_GUESS[i]:
                bulls += 1
            else:
                cows += 1
        
    # if users_guess[0] == CORRECT_GUESS[0]:
    #     bulls += 1
    # else:
    #     cows += 1
    # if users_guess[1] == CORRECT_GUESS[1]:
    #     bulls += 1
    # else:
    #     cows += 1
    # if users_guess[2] == CORRECT_GUESS[2]:
    #     bulls += 1
    # else:
    #     cows += 1
    # if users_guess[3] == CORRECT_GUESS[3]:
    #     bulls += 1
    # else:
    #     cows += 1
    print(f"Cows:{cows}")
    print(f"Bulls:{bulls}")

    


#     bulls = 0
#     cows = 0
#     if correct_guess[0] == users_guess[0]:
#         bulls += 1
#         print(f"Bulls: {bulls}")
#     elif correct_guess[0] != users_guess[0]:
#         cows += 1
#         print(f"Cows: {cows}")
#     else:
#         print("Invalid number")