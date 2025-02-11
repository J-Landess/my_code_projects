scores = 0
valid_answers = ["A","B","C","D","a","b","c","d"]
#correct_answers = {answer_1:"C",answer_2:"B",answer_3:"D"}
while True:
    try:
        answer_1 = input("What is the Capitol of France?\nA. Berlin\nB. Madrid\nC. Paris\nD. Rome\n Your answer: ").upper()
        if answer_1 not in valid_answers:
            raise ValueError()
        else:
            break
    except ValueError:
        print("please enter a, b, c, or d")   
while True:
    try:
        answer_2 = input("Question 2: Which planet is known as the red planet?\nA. Earth\nB. Mars\nC. Jupiter\nD. Saturn\n Your answer: ").upper()
        if answer_2 not in valid_answers:
            raise ValueError()
        else:
            break 
    except ValueError:
        print("please enter a, b, c, or d")  
while True:
    try:
        answer_3 = input("Question 3: What is the largest ocean on Earth?\nA. Atlantic\nB. Indian\nC. Arctic\nD. Pacific\n Your answer: ").upper()
        if answer_3 not in valid_answers:
            raise ValueError()
        else:
            break 
    except ValueError:
        print("please enter a, b, c, or d")  


correct_answers = {"Question_1":"C","Question_2":"B","Question_3":"D"}
if answer_1 == correct_answers["Question_1"]:
    scores += 1
    print("Question 1 is correct!")
else:
    print("Question 1 is incorrect")

if answer_2 == correct_answers["Question_2"]:
    scores += 1
    print("Question 2 is correct!")
else:
    print("Question 2 is incorrect")

if answer_3 in correct_answers["Question_3"]:
    scores += 1
    
    print("Question 3 is correct!")
else:
    print("Question 3 is incorrect")
    
print(f"You got {scores}/3 correct") 

