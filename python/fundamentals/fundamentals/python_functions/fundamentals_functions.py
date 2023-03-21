def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets 
                    #sent back to and saved into new_val, so we will see 8

def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

def say_hi2(name):
    return "Hi " + name

greeting = say_hi2("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable

print(greeting) # this will output 'Hi Michael'

#from add function
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

print(sum1) # => 10
print(sum2) # => 5
print(sum3) # => 15


#Default Parameters and Named Arguments

# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)

be_cheerful()    # output: good morning (repeated on 2 lines)
be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)

# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)


#Debugging

def multiply(num_list, num): #don't go inside the function until the function is called
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5) # now our function executes; what is a function call equal to?

print(b) # =>  output: [2,4,10,16]
# => and the resulting value is printed

"""
def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[2,4,10,16] 5
>>>[2,4,10,16]
"""

def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)


def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
        print("loop change value", num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b) # output: >>>[10,20,50,80]