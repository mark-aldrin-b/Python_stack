class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance+= amount
    
    def make_withdrawal(self, amount):
        self.account_balance = self.account_balance - amount 
    
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        #aldrin.trasnfer_money(smart.account_balance, 500)
        other_user.account_balance = other_user.account_balance + amount
        self.account_balance = self.account_balance - amount
        self.display_user_balance()
        other_user.display_user_balance()

aldrin = User("Aldrin Bersabe")
bolt = User("Bolt Bersabe")
smart = User("Smart and Aubrey")

aldrin.make_deposit(1000)
aldrin.make_deposit(1500)
aldrin.make_deposit(2000)
aldrin.make_withdrawal(900)

bolt.make_deposit(5000)
bolt.make_deposit(5000)
bolt.make_withdrawal(2000)

smart.make_deposit(30000)
smart.make_withdrawal(2000)
smart.make_withdrawal(2000)
smart.make_withdrawal(2000)

aldrin.display_user_balance()
bolt.display_user_balance()
smart.display_user_balance()

aldrin.transfer_money(smart, 500)