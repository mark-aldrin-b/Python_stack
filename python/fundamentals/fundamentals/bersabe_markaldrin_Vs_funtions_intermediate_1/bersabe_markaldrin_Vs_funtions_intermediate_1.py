
#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[1]['last_name'] = 'Bryant'
print(students[1])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
z[0]['y'] = 30
print(z)


#Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        print('first_name:', some_list[x]['first_name']+ ', '+ 'last_name:', some_list[x]['last_name'])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


#Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    student = {key_name: some_list}
    print(student[key_name])

iterateDictionary2('first_name', 'Michael') 
iterateDictionary2('first_name', 'John')
iterateDictionary2('first_name', 'Mark')
iterateDictionary2('first_name', 'KB')

iterateDictionary2('last_name', 'Jordan')
iterateDictionary2('last_name', 'Rosales')
iterateDictionary2('last_name', 'Guillen')
iterateDictionary2('last_name', 'Tonel')


#Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    print(len(some_dict['locations']), "LOCATIONS")
    for key in range(len(some_dict['locations'])):
        print(some_dict['locations'][key])
    
    print(len(some_dict['instructors']), "INSTRUCTORS")
    for key in range(len(some_dict['instructors'])):
        print(some_dict['instructors'][key])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

