

class Account:
    
    def __init__(self, balance=0):
        self.balance = balance
    
    def user_interface(self):
        while True:
            try:
                user_choice = int(input("\nplease select a numerical option\n1. view account\n2. add money\n3. take money\n4. exit\n"))
                if user_choice == 1:
                    user_account.show_funds()
                elif user_choice == 2:
                    user_account.add_funds()
                elif user_choice == 3:
                    user_account.subtract_funds()
                elif user_choice == 4:
                    print("Thankyou and have a nice day!")
                    break
            except ValueError:
                print("Please enter a number 1-4")
    
    def add_funds(self,):
        while True:
            try:
                amount = int(input("How much would you like to add?: "))
                if amount > 0:
                    self.balance += amount
                    print(f"\nNew Balance: ${self.balance}")
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Please enter a correct amount")
        
    
    def subtract_funds(self,):
        while True:
            try:
                amount = int(input("How much would you like to withdraw?: "))
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    print(f"\nNew Balance: ${self.balance}")
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Please enter a correct amount")
            
    
    def show_funds(self,):
        print(f"Your balance is: ${self.balance}")


user_account = Account()
user_account.user_interface()
