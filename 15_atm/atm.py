import sys
import json
import os
import random
import string
# from password_generator_v3 import get_user_params, generate
class Account:
    
    def __init__(self, balance=0,):
        self.balance = balance
        self.name = None
        self.filename = None
        self.password = None

    def user_creds(self,):
        while True:
            self.name = input("what is your name?: ").strip()
            self.filename = f"{self.name}_data.json"
            if os.path.exists(f"{self.name}_data.json"):
                with open(self.filename, "r") as file:
                    user_account = json.load(file)
                    self.balance = user_account["Balance"]
                    self.password = user_account["Password"]
                    print(f"Welcome back {self.name}")
                    password_passed = input("Please enter your password: ")
                    if password_passed == user_account["Password"]:
                        self.balance = user_account["Balance"]
                        break
                    else:
                        print("Incorrect Password") 
                       
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
                user_choice = int(input("\nplease select a numerical option\n1. view account\n2. add money\n3. take money\n4. exit\n"))
                if user_choice == 1:
                    self.show_funds()
                elif user_choice == 2:
                    self.add_funds()
                elif user_choice == 3:
                    self.subtract_funds()
                elif user_choice == 4:
                    print(f"\nThankyou {self.name} and have a nice day!\n")
                    user_account = {"Name": self.name,"Balance": self.balance, "Password": self.password}
                    with open(f"{self.filename}","w") as file:
                        json.dump(user_account, file, indent=4)
                    sys.exit()
            except ValueError:
                print("Please enter a number 1-4")
    
    def add_funds(self,):
        while True:
            try:
                amount = int(input("\nHow much would you like to add?: "))
                if amount > 0:
                    self.balance += amount
                    print(f"\nNew Balance: ${self.balance}")
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("\nPlease enter a correct amount")
        
    def subtract_funds(self,):
        while True:
            try:
                amount = int(input("\nHow much would you like to withdraw?: "))
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    print(f"\nNew Balance: ${self.balance}")
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("\nPlease enter a correct amount")
            
    def show_funds(self,):
        print(f"\n{self.name} your balance is: ${self.balance}")

def run():
    user_account = Account()
    user_account.user_creds()
    user_account.user_interface()

run()