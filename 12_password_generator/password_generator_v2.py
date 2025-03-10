import random
import string
numbers = string.digits
letters = string.ascii_letters
special_characters = string.punctuation
u_letters = letters.upper()
l_letters = letters.lower()
all_characters = numbers+letters+special_characters

def get_user_params():
    while True:
        try:
            length = int(input("How long do you want your password?: "))
            if length < 1:
                raise ValueError()
            if str(length) not in numbers:
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
        except ValueError:
            print("Please enter a correct input")
            
        return length, uppercase, lowercase, special



def generate(length,uppercase,lowercase,special):
    if uppercase == "y" and lowercase == "y" and special == "y":
        password = [random.choice(all_characters) for character in range(length)]
        print(password)
    elif uppercase == "n" and lowercase == "n" and special == "n":
        password = [random.choice(numbers) for character in range(length)]
        print(password)
    elif uppercase == "y" and lowercase == "y" and special == "n":
        password = [random.choice(u_letters + l_letters + numbers) for character in range(length)]
        print()
    elif uppercase == "y" and lowercase == "n" and special == "n":
        password = [random.choice(u_letters + numbers) for character in range(length)]
        print(password)
    elif uppercase == "n" and lowercase == "n" and special == "y":
        password = [random.choice(special_characters + numbers) for character in range(length)]
        print(password)
    elif uppercase == "n" and lowercase == "y" and special == "n":
        password = [random.choice(l_letters + numbers) for character in range(length)]
        print(password)
        return password
       


length,uppercase,lowercase,special = get_user_params()
generate(length,uppercase,lowercase,special)