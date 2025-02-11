import sys
from termcolor import colored, cprint

scores = 0
valid_answers = ["A","B","C","D",]
#correct_answers = {answer_1:"C",answer_2:"B",answer_3:"D"}

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
def run():
    scores = 0
    scores = get_answer_1(scores)         
    scores = get_answer_2(scores)
    scores = get_answer_3(scores)
    colrtxt = colored(f"GameOver you got {scores}/3 questions right","blue")
    print(f"{colrtxt}")

run()









# def compute_score(answer_1, answer_2, answer_3, scores):
#     print(scores)
#     correct_answers = {"question_1":["C","c"],"question_2":["B","b"],"question_3":["D","d"]}
#     if answer_1 in correct_answers["question_1"]:
#         scores += 1
#         text = colored("Question 1 is correct!","green",)
#         print(text)
#     else:
#         text = colored("Question 1 is incorrect","red",)
#         print(text)

#     if answer_2 in correct_answers["question_2"]:
#         scores += 1
#         text = colored("Question 2 is correct!","green",)
#         print(text)
#     else:
#         text = colored("Question 2 is incorrect","red",)
#         print(text)


#     if answer_3 in correct_answers["question_3"]:
#         scores += 1
#         text = colored("Question 3 is correct!","green",)
#         print(text)
#     else:
#         text = colored("Question 3 is incorrect","red",)
#         print(text)


#     text = colored(f"You got {scores}/3 correct","blue",attrs=["underline","blink"])
#     print(text) 
#     return scores
# correct_answers = {"question_1":["C",],"question_2":["B",],"question_3":["D",]}
# answer_1 = get_answer_1(scores)
# answer_2 = get_answer_2(scores)
# answer_3 = get_answer_3(scores)
# correct_answers = {"question_1":["C",],"question_2":["B",],"question_3":["D",]}
# scores = compute_score(answer_1, answer_2, answer_3, scores)

