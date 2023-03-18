dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce

"""
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

"""
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']
empty_list.append(ninjas)
print(empty_list)

"""
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        
"""
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
print(new_person['hobbies'][0])
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)
empty_dict['new_person'] = ['name', 'age', 'has_glasses', 'hobbies']
print(empty_dict['new_person'][3])


print(type(2)) #output: <class 'int'>
print(type(empty_list))	#output: <class 'list'>

print(len(dog))	# length (like dog.length of Js )
print(len('Coding_Dojo'))

#numbers

print(type(24))
print(type(3.9))
print(type(3j))

int_to_float = float(35)
print(int_to_float)
float_to_int = int(44.6)
print(float_to_int)
int_to_complex = complex(35)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

import random
print(random.randint(2,5)) # provides a random number between 2 and 5


#Strings

print("this is a sample string")
name = "Zen"
print("My name is", name)
name = "Zen"
print("My name is "+ name)
#print("Hello " + 42) #error
print("Hello " + '42')
print("Hello " + str(42))
print("Hello", 42)

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
print(total)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name}  {last_name} and I am {age} years old.")

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.


hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

x = "hello world" #Built-In String Methods
print(x.title())
# output:
"Hello World"

print(x.upper())
print(x.lower())


#List

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

p = [1,2,3,4,5]
p.append(99)
print(p)
#the output would be [1,2,3,4,5,99]

x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output 3
print(min(x))
print(sorted(vegetables))

for_built = [5,3,6,7,8,2]
print(for_built.extend(my_list)) #??? I don't know how this fuction
print(for_built.pop(1))
print(for_built.index(8)) #3rd index, because 3 or index[1] is pop.

stack= []
stack.append(1)
stack.append("word")
stack.append( ("a","2-tuple") )
print(stack)
print(stack[2][1])


#Tuples

tuple_letters = "a", "b", "c", "d"
print(tuple_letters)

dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")


#Dictionaries

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print(weekend)
print(capitals)

"""Accessing Values
To access the values of a dictionary, you can use the familiar square brackets 
along with the key to obtain its value.
"""
print(weekend["Sun"])
print(capitals["svk"])

"""Removing Values"""
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

"""Nested Dictionaries
Nesting is also allowed in dictionaries. Dictionaries may contain lists and tuples."""
context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}
print(context['questions'])
print(context['questions'][0]['content'])
print(context['questions'][1])
print(context['questions'][2]['id'], context['questions'][2]['content'])

print(weekend.copy())
print(weekend.values())


#Conditional

x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute
    
x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   

if not (1 <= 2 and 2 >= 3):
    print(True)
else:
    print(False)

if not (1 <= 2 and 4 >= 3):
    print(True)
else:
    print(False)


#Loops

for x in range(0, 10, 2):
    print('1st', x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print('2nd', x)
# output: 5, 2

for x in "Hello "'me':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

my_list = ["abc", 123, "xyz"]
for i in my_list:
    print(i)
# output: abc, 123, xyz

my_list = ["abc", 123, "xyz"]
for x in range(0, len(my_list)):
    print(my_list[x])
# output: 0 abc, 1 123, 2 xyz

for b in range(1, len(for_built)):
    print("for_built length", b)

for data in dog: #tuples loop
    print(data)

"""For Loops through Dictionaries
Dictionaries are also iterable. When we iterate through a dictionary, 
the iterator is each of the keys of the dictionary."""
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

"""if want to print value"""
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

capitals2 = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals2.keys():
        print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values

for val in capitals2.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values

for key, val in capitals2.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r  => Notice that when the loop got to the letter "i", we stopped looping.

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1