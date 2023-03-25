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

