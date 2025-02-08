


valid_answers = ["A","B","C","D","a","b","c","d"]
correct_answers = {answer_1:"C",answer_2:"B",answer_3:"D"}
while True:
    try:
        answer_1 = input("What is the Capitol of France?\nA. Berlin\nB. Madrid\nC. Paris\nD. Rome\n Your answer: ")
        if answer_1 not in valid_answers:
            raise ValueError()
        else:
            break
    except ValueError:
        print("please enter a, b, c, or d")   
while True:
    try:
        answer_2 = input("Question 2: Which planet is known as the red planet?\nA. Earth\nB. Mars\nC. Jupiter\nD. Saturn\n Your answer: ")
        if answer_2 not in valid_answers:
            raise ValueError()
        else:
            break 
    except ValueError:
        print("please enter a, b, c, or d")  
while True:
    try:
        answer_3 = input("Question 3: What is the largest ocean on Earth?\nA. Atlantic\nB. Indian\nC. Arctic\nD. Pacific\n Your answer: ")
        if answer_3 not in valid_answers:
            raise ValueError()
        else:
            break 
    except ValueError:
        print("please enter a, b, c, or d")  

correct_answers = {answer_1:"C",answer_2:"B",answer_3:"D"}


# A. Berlin
# B. Madrid
# C. Paris
# D. Rome
# Your answer:
# either print correct or not 

# Question 2: Which planet is known as the red planet?
# A. Earth
# B. Mars
# C. Jupiter
# D. Saturn
# Your answer:
# either print correct or not

# Question 3: What is the largest ocean on Earth?
# A. Atlantic
# B. Indian
# C. Arctic
# D. Pacific
# Your answer:
# either print corrrect or not

# Compute scores and print results