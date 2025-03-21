
import random
import string
numbers = string.digits
letters = string.ascii_letters
special_characters = string.punctuation
u_letters = letters.upper()
l_letters = letters.lower()
all_characters = numbers+letters+special_characters
character_set = numbers
def get_user_params():
    while True:
        try:
            length_str = input("How long do you want your password?: ")
            length = int(length_str)

            if length < 1:
                raise ValueError()
            uppercase = input("include uppercase letters [y/n]?: ").lower()
            if uppercase not in ["y","n"]:
                raise ValueError()   
            lowercase = input("include lowercase letters [y/n]?: ").lower()
            if lowercase not in ["y","n"]:
                raise ValueError()
            special = input("include special characters [y/n]?: ").lower()
            if special not in ["y","n"]:
                raise ValueError()
            return length, uppercase, lowercase, special
        except ValueError:
            print("Please start over and enter a correct input....")
            
def generate(length, uppercase, lowercase, special):
    character_set = numbers
    try:
        if uppercase == "y":
            character_set += u_letters 
            password = [random.choice(character_set) for character in range(length)]
        if lowercase == "y":
            character_set += l_letters
            password = [random.choice(character_set) for character in range(length)]
        if special == "y":
            character_set += special_characters
            password = [random.choice(character_set) for character in range(length)]
            print("".join(password))
            return "".join(password)
        else:
            password = [random.choice(character_set) for character in range(length)]
            print("".join(password))
            return "".join(password)
    except TypeError:
        print("Invalid entry")    
# def run():
#     length,uppercase,lowercase,special = get_user_params()
#     password = generate(length,uppercase,lowercase,special)
#     print(f"Password: {password}")
#     return password

# run()