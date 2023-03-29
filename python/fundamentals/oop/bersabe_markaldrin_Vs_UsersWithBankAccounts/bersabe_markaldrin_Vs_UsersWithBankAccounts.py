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
            self.balance = self.balance + (self.balance * self.interest_rate)
        return self
checking = BankAccount(0.05, 0)
saving = BankAccount(0.05, 0)


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0,balance=0)
        self.create_account = {"Savings": 0} 
        self.create_account_c = {"Checking": 0}
    def make_deposit(self, amount, accnt):
        if accnt == 0:
            self.create_account = self.create_account["Savings"] + amount
        elif accnt == 1:
            self.create_account_c = self.create_account_c["Checking"] + amount
        return self
    
    def make_withdrawal(self, amount):
        if self.create_account > 0:
            self.create_account = self.create_account["Savings"] - amount
        if self.create_account_c > 0:
            self.create_account_c = self.create_account_c["Checking"] - amount
        return self
    
    def display_user_balance(self):
        if self.create_account > 0:
            print(f"User:{self.name}, Savings Balance: {self.create_account}")
        if self.create_account_c > 0:
            print(f"User:{self.name}, Checking Balance: {self.create_account_c}")
        return self
        
    def transfer_money(self, other_user, amount):
        other_user.account = other_user.account.balance + amount
        self.account = self.account.balance - amount
        
        self.display_user_balance()
        other_user.display_user_balance()
        return self
        
        

aldrin = User("Aldrin Bersabe")

aldrin.make_deposit(1000, 0).make_deposit(1000, 1).display_user_balance()



