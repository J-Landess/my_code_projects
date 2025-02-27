from termcolor import colored
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
def get_answer():
    CORRECT_GUESS = random.sample(range(0, 9), 4)
    print(CORRECT_GUESS)
    return CORRECT_GUESS

def get_user_guess():
    users_guess = [int(i) for i in input("Guess a four digit number: ")]
    if len(users_guess) == 4:
        return users_guess 
    else:
        print("please enter only four digits!!!!")
        get_user_guess()
    
def compute(CORRECT_GUESS,users_guess):
    cows = 0
    bulls = 0
    for i in range(4):
            if users_guess[i] == CORRECT_GUESS[i]:
                bulls += 1
            else:
                cows += 1
    if bulls == 4:
        text = colored("Correct!!!!","green")
        print(text)
    return cows, bulls
     
def check_win(bulls):
    if bulls > 3:
        return True

def print_score(cows, bulls):
    colored_cows = colored("Cows","red")
    colored_bulls = colored("bulls","blue")
    print(f"{colored_cows}:{cows}\n{colored_bulls}:{bulls}")    

def run():
     bulls = 0
     cows = 0
     CORRECT_GUESS = get_answer()
     while not check_win(bulls):
        users_guess = get_user_guess()
        cows, bulls = compute(CORRECT_GUESS, users_guess)
        score = print_score(cows, bulls)
        print(score)


run()





# # print(type(CORRECT_GUESS[:4]))
# # print(CORRECT_GUESS[:4])
# while True:
#     cows = 0
#     bulls = 0
#     try:
#         users_guess = [int(i) for i in input("Guess a four digit number: ")]
#         # if user_guess == "q":
#         #     break
    
#         print(users_guess)
#         print(type(users_guess))
#     except ValueError:
#         print("Please enter four non repeating numbers: ")
    
#     for i in range(4):
#             if users_guess[i] == CORRECT_GUESS[i]:
#                 bulls += 1
#             else:
#                 cows += 1
#     if bulls == 4:
#         print(f"Correct!!!")
#         break
      
#     # if users_guess[0] == CORRECT_GUESS[0]:
#     #     bulls += 1
#     # else:
#     #     cows += 1
#     # if users_guess[1] == CORRECT_GUESS[1]:
#     #     bulls += 1
#     # else:
#     #     cows += 1
#     # if users_guess[2] == CORRECT_GUESS[2]:
#     #     bulls += 1
#     # else:
#     #     cows += 1
#     # if users_guess[3] == CORRECT_GUESS[3]:
#     #     bulls += 1
#     # else:
#     #     cows += 1
#     print(f"Cows:{cows}")
#     print(f"Bulls:{bulls}")

    


# #     bulls = 0
# #     cows = 0
# #     if correct_guess[0] == users_guess[0]:
# #         bulls += 1
# #         print(f"Bulls: {bulls}")
# #     elif correct_guess[0] != users_guess[0]:
# #         cows += 1
# #         print(f"Cows: {cows}")
# #     else:
# #         print("Invalid number")