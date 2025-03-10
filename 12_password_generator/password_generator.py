import random
import string
numbers = string.digits
letters = string.ascii_letters
special_characters = string.punctuation
u_letters = letters.upper()
l_letters = letters.lower()
all_characters = numbers+letters+special_characters
# enter password length
length = int(input("How long do you want your password?: "))
uppercase = input("include uppercase letters [y/n]?: ")
lowercase = input("include lowercase letters [y/n]?: ")
special = input("include special characters [y/n]?: ")

if uppercase == "y" and lowercase == "y" and special == "y":
    for i in range(length):
        password = [random.choice(all_characters) for character in range(length)]
    print(password)
elif uppercase == "n" and lowercase == "n" and special == "n":
    for i in range(length):
        password = [random.choice(numbers) for character in range(length)]
    print(password)
elif uppercase == "y" and lowercase == "y" and special == "n":
    for i in range(length):
        password = [random.choice(u_letters + l_letters + numbers) for character in range(length)]
    print(password)
elif uppercase == "y" and lowercase == "n" and special == "n":
    for i in range(length):
        password = [random.choice(u_letters + numbers) for character in range(length)]
    print(password)
elif uppercase == "n" and lowercase == "n" and special == "y":
    for i in range(length):
        password = [random.choice(special_characters + numbers) for character in range(length)]
    print(password)
elif uppercase == "n" and lowercase == "y" and special == "n":
    for i in range(length):
        password = [random.choice(l_letters + numbers) for character in range(length)]
    print(password)

