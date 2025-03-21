from termcolor import colored
import sys
import json
import os



class Account:
    """This is a class that mimicks an online bank account and saves different users information in a JSON file."""
    
    def __init__(self, balance=0,):
        self.balance = balance
        self.name = None
        self.filename = None
        self.password = None
    
    def __str__(self,):
        return f"{colored(f'${self.balance}', 'green', 'on_black',['bold'])}"

    def user_creds(self,):
        while True:
            self.name = input("What is your name?: ").strip()
            self.filename = f"{self.name}_data.json"
            if os.path.exists(f"{self.name}_data.json"):
                with open(self.filename, "r") as file:
                    user_account = json.load(file)
                    self.balance = user_account["Balance"]
                    self.password = user_account["Password"]
                    print(f"{colored('\nWelcome back', 'light_blue')} {colored(self.name,'light_blue')}")
                    password_passed = input("Please enter your password: ")
                    if password_passed == user_account["Password"]:
                        self.balance = user_account["Balance"]
                        print(f"{colored("Password accepted","light_blue")}")
                        break
                    else:
                        print(f"{colored("Incorrect Password","red",'on_black',['bold','blink'])}")          
            else:
                self.password = input("Please choose a password: ")
                user_account = {"Name": self.name, "Balance": self.balance,"Password": self.password}
                self.filename = f"{self.name}_data.json"
                with open(self.filename,"w") as file:
                    json.dump(user_account, file, indent=4)
                    print(f"Account saved to {self.filename}")
                break
    
    def user_interface(self,):
        while True:
            try:
                user_choice = int(input("\nWelcome to your banking system\nPlease select an Option:\n\n1. View Account\n2. Deposit\n3. Withdraw funds\n4. Exit\n"))
                if user_choice == 1:
                    hidden_password = ["*" for _ in range(len(self.password))]
                    hidden_password = " ".join(hidden_password)
                    print(f"\nName: {self.name}\nPassword: {hidden_password}")
                    self.show_funds()
                elif user_choice == 2:
                    self.add_funds()
                elif user_choice == 3:
                    self.subtract_funds()
                elif user_choice == 4:
                    print(f"{colored('Thankyou', 'light_blue',)} {colored(self.name,'light_blue')} {colored('and have a great day', 'light_blue')}")
                    
                    user_account = {"Name": self.name,"Balance": self.balance, "Password": self.password}
                    with open(f"{self.filename}","w") as file:
                        json.dump(user_account, file, indent=4)
                    sys.exit()
            except ValueError:
                print("Please enter a number 1-4")
    
    def add_funds(self,):
        while True:
            try:
                amount = float(input("\nHow much would you like to add?: "))
                if amount > 0:
                    self.balance += amount
                    print(f"\nNew Balance: {self}")
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("\nPlease enter a correct amount")
        
    def subtract_funds(self,):
        while True:
            try:
                amount = float(input("\nHow much would you like to withdraw?: "))
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    print(f"\nNew Balance: {self}")
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("\nPlease enter a correct amount")
            
    def show_funds(self,):
        
        print(f"\n{self.name} your balance is: {self}")

def run():
    user_account = Account()
    user_account.user_creds()
    user_account.user_interface()

run()