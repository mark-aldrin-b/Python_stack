class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance+= amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance = self.account_balance - amount 
        return self
    
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account_balance}")
        return self
        
    def transfer_money(self, other_user, amount):
        #aldrin.trasnfer_money(smart.account_balance, 500)
        other_user.account_balance = other_user.account_balance + amount
        self.account_balance = self.account_balance - amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

aldrin = User("Aldrin Bersabe")
bolt = User("Bolt Bersabe")
smart = User("Smart and Aubrey")

aldrin.make_deposit(1000).make_deposit(1500).make_deposit(2000).make_withdrawal(900).display_user_balance()

bolt.make_deposit(5000).make_deposit(5000).make_withdrawal(2000).display_user_balance()

smart.make_deposit(30000).make_withdrawal(2000).make_withdrawal(2000).make_withdrawal(2000).display_user_balance()

aldrin.transfer_money(smart, 500)
