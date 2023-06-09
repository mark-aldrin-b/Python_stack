#CLASSES
"""
# declare a class and give it name User
class User:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty """

"""
michael = User()
anna = User()"""

"""
class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    # we assign them accordingly
        self.name = name
        self.email = email_address
    # the account balance is set to $0
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)

print(guido.name,"=>", guido.email,"=>", guido.bank_name,"=>",guido.account_balance)	# output: Guido van Rossum
print(monty.name, monty.account_balance)	# output: Monty Python # output: 50

print(monty.account_balance)	# output: 50


# Class/Static Method
    #@Classmethod
class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
            # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

print(BankAccount.bank_name)

aldrin = BankAccount(5, 500)
bolt = BankAccount(5, 1000)
print(BankAccount.all_accounts)

print(BankAccount.all_balances())
aldrin.change_bank_name("Bank ni Bolt")

print(aldrin.bank_name)
"""

"""
    #@staticmethod

class BankAccount:
    # ... __init__ goes here
    def __init__(self, name,):
        self.name = name
        self.balance = 0
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
        

aldrin = BankAccount("Aldrin")
aldrin.with_draw(500)
print(aldrin.can_withdraw(0, 500))
"""


#Association Between classes


#Four Pillars
"""
class Barista:
    def __init__(self,name,CoffeeM):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()

user = Barista("Mark", "espresso")
print(user.make_coffee)


class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self
    

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	
        self.is_roth = is_roth	
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self
        """


    
# import the library
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)