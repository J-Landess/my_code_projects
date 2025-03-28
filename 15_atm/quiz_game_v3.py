import sys
from termcolor import colored, cprint


valid_answers = ["A","B","C","D",]

def get_answer_1(scores=0):
    while True:
        try:
            answer_1 = input("What is the Capitol of France?\nA. Berlin\nB. Madrid\nC. Paris\nD. Rome\n Your answer: ").upper()
            correct_answers = {"answer_1":"C","answer_2":"B","answer_3":"D"}
            if answer_1 not in valid_answers:
                raise ValueError()
            elif answer_1 in correct_answers["answer_1"]:
                text = colored("Question 1 is correct!","green",)
                scores += 1
                print(text)
                break 
            else:
                text = colored("Wrong Answer","red") 
                print(text) 
                break
        except ValueError:
            print("please enter a, b, c, or d")   
    return scores    
def get_answer_2(scores):
    while True:
        try:
            answer_2 = input("Question 2: Which planet is known as the red planet?\nA. Earth\nB. Mars\nC. Jupiter\nD. Saturn\n Your answer: ").upper()
            correct_answers = {"answer_1":"C","answer_2":"B","answer_3":"D"}
            if answer_2 not in valid_answers:
                raise ValueError()
            elif answer_2 in correct_answers["answer_2"]:
                text = colored("Question 2 is correct!","green",)
                scores += 1
                print(text)
                break
            else:
                text = colored("Wrong Answer","red") 
                print(text) 
                break
        except ValueError:
            print("please enter a, b, c, or d")   
    return scores      
      
def get_answer_3(scores):
    while True:
        try:
            answer_3 = input("Question 3: What is the largest ocean on Earth?\nA. Atlantic\nB. Indian\nC. Arctic\nD. Pacific\n Your answer: ").upper()
            correct_answers = {"answer_1":"C","answer_2":"B","answer_3":"D"}
            if answer_3 not in valid_answers:
                raise ValueError()
            elif answer_3 in correct_answers["answer_3"]:
                text = colored("Question 2 is correct!","green",)
                scores += 1
                print(text)
                break
            else:
                text = colored("Wrong Answer","red") 
                print(text) 
                break
        except ValueError:
            print("please enter a, b, c, or d")   
    return scores         
def quiz_game():
    valid_answers = ["A","B","C","D",]
    scores = 0
    scores = get_answer_1(scores)         
    scores = get_answer_2(scores)
    scores = get_answer_3(scores)
    colrtxt = colored(f"GameOver you got {scores}/3 questions right","blue")
    print(f"{colrtxt}")
    return None

