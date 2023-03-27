
class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "Banco"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.interest_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self
        
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.interest_rate
        return self
    
    @classmethod
    def get_instances_bank(cls):
        print(f"Bank name: {cls.bank_name}, All accounts:{cls.all_accounts}")
            

aldrin = BankAccount(0.05, 0)
bolt = BankAccount(0.05, 0)

aldrin.deposit(500).deposit(500).deposit(500).yield_interest().display_account_info()

bolt.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

BankAccount.get_instances_bank()