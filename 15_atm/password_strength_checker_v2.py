# special_characters = ['!','@','#','$','%','^','&','*','(',')',]
# numbers = ['1','2','3','4','5','6','7','8','9','0',]
def get_password():
    user_password = input("Please enter a Password: ")
    return user_password


def compute_score(user_password):
    special_characters = ['!','@','#','$','%','^','&','*','(',')',]
    numbers = ['1','2','3','4','5','6','7','8','9','0',]
    password_strength = 0
    if len(user_password) > 4:
        print("\nLength + 4: Check")
        password_strength += 1 
    # print(password_strength)
    if len(user_password) > 8:
        print("\nLength + 8: Check")
        password_strength += 1
    # print(password_strength)

    if any(i in user_password for i in special_characters):
        print("\nSpecial Characters: Check")  
        password_strength += 1
        # print(password_strength)
    if any(i in user_password for i in user_password.upper()):
        print("\nUppercase: Check") 
        password_strength += 1
        # print(password_strength)
    if any(i in user_password for i in numbers):
        print("\nNumber: Check")
        password_strength += 1
        return password_strength



def checker(password_strength):
    if password_strength == None:
        print("must at least contain four characters")
        get_password()
    if password_strength == 1:
        print("Weak try again")
        get_password()
    if password_strength == 2:
        print("Fair")
    if password_strength == 3:
        print("Good")
    if password_strength == 4:
        print("Very Good") 
    if password_strength == 5:
        print("Very Strong")

def run():
    user_password = get_password()
    password_strength = compute_score(user_password)
    checker(password_strength)

# run()