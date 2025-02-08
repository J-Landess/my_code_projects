import random



class Dice:
    def __init__(self,):
        pass
       

    def roll(self):
        randint_1 = random.randint(1,6)
        randint_2 = random.randint(1,6)
        print(f'{randint_1},{randint_2}')


while True:
    
    prompt = input("Would you like to roll the dice?[y/n]: ")
    if prompt.lower() == "y":
        roll_dice = Dice()
        result = roll_dice.roll()
        
    
    elif prompt.lower() == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid Choice!")
    

        
    

